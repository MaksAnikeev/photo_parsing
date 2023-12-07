import asyncio
import os
import aiofiles


async def archive(folder=None, files=None):
    if folder:
        files_names = os.listdir(folder)
        files = [f'{folder}/{file}' for file in files_names]

    zip_command = ['zip', '-r', '-9', '-', *files]

    zip_process = await asyncio.create_subprocess_exec(*zip_command,
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)
    full_binar_archive = b''
    while True:
        part_of_archive = await zip_process.stdout.read(n=300000)
        if not part_of_archive:
            break
        full_binar_archive += part_of_archive
    return full_binar_archive


async def main():
    photo_content = await asyncio.create_task(archive(folder='for_archive'))
    # photo_content = await asyncio.create_task(archive(files=['test.py']))
    async with aiofiles.open("photos.zip", mode="wb") as zip_file:
        await zip_file.write(photo_content)


asyncio.run(main())
