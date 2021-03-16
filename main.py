import asyncio
import curses
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        # canvas.addstr(row, column, symbol, curses.A_DIM)
        # await asyncio.sleep(0)
        #
        # canvas.addstr(row, column, symbol)
        # await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def blinker(coroutine, blink_time):
    coroutine.send(None)
    time.sleep(blink_time)


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    coroutines = [blink(canvas=canvas,
                        row=5,
                        column=10),
                  blink(canvas=canvas,
                        row=5,
                        column=12),
                  blink(canvas=canvas,
                        row=5,
                        column=14),
                  blink(canvas=canvas,
                        row=5,
                        column=16),
                  blink(canvas=canvas,
                        row=5,
                        column=18)]
    blink_times = [1, 0.3, 0.5, 2]
    while True:
        for blink_time in blink_times:
            for coroutine in coroutines:
                # blinker(coroutine=coroutine, blink_time=blink_time)
                coroutine.send(None)
                canvas.refresh()

            time.sleep(blink_time)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)

# def draw(canvas):
#     canvas.border()
#     curses.curs_set(False)
#     row, column = (5, 20)
#     coroutine = blink(canvas=canvas,
#                       row=row,
#                       column=column)
#     blink_times = [1, 0.3, 0.5, 2]
#     while True:
#         for blink_time in blink_times:
#             blinker(coroutine=coroutine, blink_time=blink_time)
#             canvas.refresh()
