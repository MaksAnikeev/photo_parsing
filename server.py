# -*- coding: utf-8 -*-

from aiohttp import web
import asyncio
import os
import aiofiles
import datetime
import logging
import argparse
from environs import Env


async def archive(request):
    folder_name = request.match_info.get('archive_hash')
    try:
        folder_path = os.path.join(photo_archive_path, folder_name)
        files = os.listdir(folder_path)
    except:
        raise web.HTTPNotFound(text='404: Not Found \nАрхив не существует или был удален')

    zip_command = ['zip', '-r', '-9', '-', *files]

    zip_process = await asyncio.create_subprocess_exec(*zip_command, cwd=folder_path,
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)

    response = web.StreamResponse()
    response.headers['Content-Type'] = 'application/zip'
    response.headers['Content-Disposition'] = 'attachment; filename = "photo_archive.zip"'

    chunk = 0
    await response.prepare(request)
    try:
        while True:
            chunk += 1
            part_of_archive = await zip_process.stdout.read(300000)
            if not part_of_archive:
                break
            await response.write(part_of_archive)
            logging.info(f'Sending archive chunk {chunk}')

            # if chunk == 5:
            #     raise SystemExit()

            await asyncio.sleep(INTERVAL_SECS)
    except ConnectionResetError:
        logging.info('CancelledError')
        raise
    finally:
        logging.info('Download was finished or interrupted')
        # web.close()

    return response




async def handle_index_page(request):
    async with aiofiles.open('index.html', mode='r') as index_file:
        index_contents = await index_file.read()
    return web.Response(text=index_contents, content_type='text/html')


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('delay',
    #                     type=int,
    #                     nargs='?',
    #                     help='задержка по загрузке частей архива',
    #                     default=0)
    # parser.add_argument('logging',
    #                     nargs='?',
    #                     help='включение логирования',
    #                     default=False)
    # parser.add_argument('archive_path',
    #                     nargs='?',
    #                     help='папка где хранятся архивы фотографий',
    #                     default='test_photos')
    #
    # args = parser.parse_args()
    #
    # INTERVAL_SECS = args.folder

    # if args.logging:
    #     logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    #                         level=logging.DEBUG)

    env = Env()
    env.read_env()

    INTERVAL_SECS = env.int('INTERVAL_SECS', 0)
    switch_logging = env.bool('LOGGING', False)
    photo_archive_path = env('ARCHIVE_PATH', 'test_photos')

    if switch_logging:
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG)
    app = web.Application()
    app.add_routes([
        web.get('/', handle_index_page),
        web.get('/archive/{archive_hash}/', archive),
    ])
    web.run_app(app)
