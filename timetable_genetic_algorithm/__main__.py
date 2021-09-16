import sys
import json


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

    async def generate_timetable(request):
        response_obj = {'status': 'success'}
        web.Response(text=json.dumps(response_obj), status=200)
        # server_entry_point()

    app = web.Application()
    app.router.add_get('/generate', generate_timetable)
    web.run_app(app)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        console_main()
    else:
        server_main()
