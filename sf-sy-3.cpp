#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

typedef struct 
{
    int id;   
    int x;
    int y;
} Point;

typedef struct pS 
{
    int iC1, iC2;  // 两个点的编号
    float fD;      // 两点距离
} pT;

// 计算两点距离
float dist(Point a, Point b) 
{
    int dx = a.x - b.x;
    int dy = a.y - b.y;
    return sqrt((float)(dx * dx + dy * dy));
}

// 暴力法
pT bruteForce(Point p[], int n) 
{
    pT res;
    res.fD = FLT_MAX;
    for (int i = 0; i < n; i++) 
	{
        for (int j = i + 1; j < n; j++) 
		{
            float d = dist(p[i], p[j]);
            if (d < res.fD) {
                res.fD = d;
                res.iC1 = p[i].id;
                res.iC2 = p[j].id;
            }
        }
    }
    return res;
}

// 按x坐标排序
int cmpX(const void *a, const void *b) 
{
    Point *p1 = (Point *)a;
    Point *p2 = (Point *)b;
    return p1->x - p2->x;
}

// 按y坐标排序
int cmpY(const void *a, const void *b) 
{
    Point *p1 = (Point *)a;
    Point *p2 = (Point *)b;
    return p1->y - p2->y;
}

pT minP(pT a, pT b) 
{
    return (a.fD < b.fD) ? a : b;
}

// 分治法
pT closest(Point p[], int l, int r) 
{
    if (r - l + 1 <= 3) 
	{
        return bruteForce(p + l, r - l + 1);
    }

    int mid = (l + r) / 2;
    int midX = p[mid].x;

    pT left = closest(p, l, mid);
    pT right = closest(p, mid + 1, r);
    pT best = minP(left, right);

    Point strip[r - l + 1];
    int k = 0;
    for (int i = l; i <= r; i++) 
	{
        if (abs(p[i].x - midX) < best.fD) 
		{
            strip[k++] = p[i];
        }
    }

    qsort(strip, k, sizeof(Point), cmpY);

    for (int i = 0; i < k; i++) 
	{
        for (int j = i + 1; j < k && (strip[j].y - strip[i].y) < best.fD; j++) 
		{
            float d = dist(strip[i], strip[j]);
            if (d < best.fD) 
			{
                best.fD = d;
                best.iC1 = strip[i].id;
                best.iC2 = strip[j].id;
            }
        }
    }
    return best;
}

int main() 
{
   
    int PN[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int PX[10] = {-11, 15, 4, -5, 2, 3, -2, -7, -4, 10};
    int PY[10] = {4, -3, 6, -6, -1, 2, 7, 5, -7, 0};
    int n = 10;

    Point pts[10];
    for (int i = 0; i < n; i++) 
	{
        pts[i].id = PN[i];
        pts[i].x = PX[i];
        pts[i].y = PY[i];
    }

    pT res1 = bruteForce(pts, n);
    printf("暴力法: 点%d 和 点%d, 距离 = %.2f\n", res1.iC1, res1.iC2, res1.fD);

    Point pts2[10];
    for (int i = 0; i < n; i++) pts2[i] = pts[i];
    qsort(pts2, n, sizeof(Point), cmpX);   
    pT res2 = closest(pts2, 0, n - 1);
    printf("分治法: 点%d 和 点%d, 距离 = %.2f\n", res2.iC1, res2.iC2, res2.fD);

    return 0;
}