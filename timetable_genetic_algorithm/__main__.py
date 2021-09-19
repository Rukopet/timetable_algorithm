import logging
import sys
import json

from timetable_genetic_algorithm import config


def console_main():
    from timetable_genetic_algorithm.utils.tmp_main import console_entry_point
    len_argv = len(sys.argv)
    if len_argv > 3:
        raise AttributeError(f'Incorrect argv len; your len={len_argv - 1}; need 2 or 1')
    elif len_argv == 3:
        console_entry_point(sys.argv[1], sys.argv[2])
    elif len_argv == 2:
        console_entry_point(sys.argv[1])


def server_main():
    from aiohttp import web
    from timetable_genetic_algorithm.utils.tmp_main import server_entry_point
    from timetable_genetic_algorithm.server_utils import send_email

    async def generate_timetable(request):
        try:
            request_data = await request.json(encoding='utf-8')
            print(request_data)
            response_obj = {'status': 'success', 'file_type': 'xls'}
            file, filename = server_entry_point(request_data)
            logging.info(f'file={file} || filename={filename}')
            send_email(request_data["client_email"], file, filename)

            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as e:
            response_obj = {'status': 'failure', 'description': e}
            logging.error(
                f'error -> {response_obj}'
                f'============================================='
            )
            return web.Response(text=json.dumps(response_obj), status=400)

    app = web.Application()
    app.router.add_post('/generate', generate_timetable)
    web.run_app(app, port=int(config.ALGORITHM_PORT_IN))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        console_main()
    else:
        server_main()
