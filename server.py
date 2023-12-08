# -*- coding: utf-8 -*-

from aiohttp import web
import asyncio
import os
import aiofiles
import datetime

INTERVAL_SECS = 0


async def archive(request):
    folder_name = request.match_info.get('archive_hash')
    folder_path = os.path.join('test_photos', folder_name)
    files = os.listdir(folder_path)

    zip_command = ['zip', '-r', '-9', '-', *files]

    zip_process = await asyncio.create_subprocess_exec(*zip_command, cwd=folder_path,
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)

    response = web.StreamResponse()
    response.headers['Content-Type'] = 'application/zip'
    response.headers['Content-Disposition'] = 'attachment; filename = "photo_archive.zip"'


    await response.prepare(request)

    while True:
        part_of_archive = await zip_process.stdout.read(300000)
        if not part_of_archive:
            break
        await response.write(part_of_archive)
        await asyncio.sleep(INTERVAL_SECS)

    return response




async def handle_index_page(request):
    async with aiofiles.open('index.html', mode='r') as index_file:
        index_contents = await index_file.read()
    return web.Response(text=index_contents, content_type='text/html')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/', handle_index_page),
        web.get('/archive/{archive_hash}/', archive),
    ])
    web.run_app(app)
