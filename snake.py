#include <windows.h>
#include <stdlib.h>
#include <time.h>

#define CELL_SIZE 20
#define WIDTH 30
#define HEIGHT 20
#define MAX_SEG 10

HWND hwnd;

/* snake state */
int segcount = 4;
int hx = 5, hy = 5;
int oldhx, oldhy;
int dirx = 1, diry = 0;

/* segments */
int sgx[MAX_SEG], sgy[MAX_SEG];

/* food */
int bx, by;

/* --------- drawing ---------- */

void draw_cell(int x, int y, COLORREF c) {
    HDC hdc = GetDC(hwnd);
    HBRUSH b = CreateSolidBrush(c);
    RECT r = { x*CELL_SIZE, y*CELL_SIZE,
               (x+1)*CELL_SIZE, (y+1)*CELL_SIZE };
    FillRect(hdc, &r, b);
    DeleteObject(b);
    ReleaseDC(hwnd, hdc);
}

void clear_screen(void) {
    HDC hdc = GetDC(hwnd);
    RECT r;
    GetClientRect(hwnd, &r);
    FillRect(hdc, &r, (HBRUSH)(COLOR_WINDOW+1));
    ReleaseDC(hwnd, hdc);
}

/* --------- game logic ---------- */

void spawn_food(void) {
    bx = rand() % WIDTH;
    by = rand() % HEIGHT;
}

void move_snake(void) {
    int i;

    /* shift tail */
    for (i = segcount - 1; i > 0; i--) {
        sgx[i] = sgx[i - 1];
        sgy[i] = sgy[i - 1];
    }

    /* first segment gets old head */
    if (segcount > 0) {
        sgx[0] = oldhx;
        sgy[0] = oldhy;
    }
}

void draw_snake(void) {
    int i;
    draw_cell(hx, hy, RGB(0, 255, 0));   /* head */

    for (i = 0; i < segcount; i++) {
        draw_cell(sgx[i], sgy[i], RGB(0, 180, 0));
    }
}

void update(void) {
    oldhx = hx;
    oldhy = hy;

    hx += dirx;
    hy += diry;

    if (hx < 0) hx = WIDTH - 1;
    if (hx >= WIDTH) hx = 0;
    if (hy < 0) hy = HEIGHT - 1;
    if (hy >= HEIGHT) hy = 0;

    move_snake();

    if (hx == bx && hy == by) {
        if (segcount < MAX_SEG)
            segcount++;
        spawn_food();
    }
}

/* --------- window ---------- */

LRESULT CALLBACK WndProc(HWND h, UINT m, WPARAM w, LPARAM l) {
    if (m == WM_KEYDOWN) {
        if (w == VK_UP    && diry == 0) { dirx = 0; diry = -1; }
        if (w == VK_DOWN  && diry == 0) { dirx = 0; diry =  1; }
        if (w == VK_LEFT  && dirx == 0) { dirx = -1; diry = 0; }
        if (w == VK_RIGHT && dirx == 0) { dirx =  1; diry = 0; }
    }
    if (m == WM_DESTROY) PostQuitMessage(0);
    return DefWindowProc(h, m, w, l);
}

/* --------- entry ---------- */

int WINAPI WinMain(HINSTANCE hi, HINSTANCE hp, LPSTR lp, int sc) {
    WNDCLASS wc = {0};
    MSG msg;

    srand((unsigned)time(0));

    wc.lpfnWndProc = WndProc;
    wc.hInstance = hi;
    wc.lpszClassName = "SnakeWin";
    RegisterClass(&wc);

    hwnd = CreateWindow(
        "SnakeWin", "Snake",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT,
        WIDTH*CELL_SIZE+16, HEIGHT*CELL_SIZE+39,
        0, 0, hi, 0
    );

    ShowWindow(hwnd, sc);
    spawn_food();

    while (1) {
        while (PeekMessage(&msg, 0, 0, 0, PM_REMOVE)) {
            if (msg.message == WM_QUIT) return 0;
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }

        update();
        clear_screen();
        draw_snake();
        draw_cell(bx, by, RGB(255, 0, 0));

        Sleep(120);
    }
}
