#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

typedef uint num_t;

typedef struct {
  num_t* array;
  uint len;
} SORT_PROTO;

void columnsort(num_t **a, uint s, uint r);

static int
comp(const void *a, const void *b)
{
  num_t *na = (num_t *)a;
  num_t *nb = (num_t *)b;
  if (*na > *nb) {
    return 1;
  }
  if (*na < *nb) {
    return -1;
  }
  return 0;
}

static void *
sort_column(void *arg)
{
  SORT_PROTO *p;
  p = (SORT_PROTO *)arg;
  qsort(p->array, (size_t)(p->len), sizeof(num_t), comp);
  return (void *)0;
}

static void
sort_columns(SORT_PROTO* p, uint s)
{
  uint i;
  pthread_t *pt;
  void *ret;
  pt = malloc(s * sizeof(pthread_t));
  for (i = 0; i < s; ++i) {
    pthread_create(pt + i, NULL, sort_column, p + i);
  }
  for (i = 0; i < s; ++i) {
    pthread_join(pt[i], &ret);
  }
  free(pt);
}

static void
display_columns(num_t **a, uint s, uint r)
{
  uint i, j;
  for (i = 0; i < s; ++i) {
    for (j = 0; j < r; ++j) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
}

void
columnsort(num_t **a, uint s, uint r)
{
  num_t **b;
  uint i, j, idx;
  SORT_PROTO *p;
  if (r % 2 != 0) {
    fprintf(stderr, "invalid input: row %d is not even.", r);
    exit(1);
  }
  if (r % s != 0) {
    fprintf(stderr, "invalid input: column %d not divide row %d.\n", s, r);
    exit(1);
  }
  if (r < 2 * s * s) {
    fprintf(stderr, "invalid input: row %d is not large enough to satisfy column "
            "%d.\n", r, s);
    exit(1);
  }
  p = malloc((s + 1) * sizeof(SORT_PROTO));
  for (i = 0; i < s; ++i) {
    p[i].array = a[i];
    p[i].len = r;
  }
  sort_columns(p, s);
  b = malloc((s + 1) * sizeof(num_t *));
  for (i = 0; i < s; ++i) {
    b[i] = malloc(r * sizeof(num_t));
    for (j = 0; j < r; ++j) {
      idx = s * j + i;
      b[i][j] = a[idx / r][idx % r];
    }
  }
  for (i = 0; i < s; ++i) {
    p[i].array = b[i];
    p[i].len = r;
  }
  sort_columns(p, s);
  for (i = 0; i < s; ++i) {
    for (j = 0; j < r; ++j) {
      idx = s * j + i;
      a[idx / r][idx % r] = b[i][j];
    }
  }
  for (i = 0; i < s; ++i) {
    p[i].array = a[i];
    p[i].len = r;
  }
  sort_columns(p, s);
  for (j = 0; j < r / 2; ++j) {
    b[0][j] = a[0][j];
  }
  p[0].array = b[0];
  p[0].len = r / 2;
  b[s] = malloc(r * sizeof(num_t));
  for (j = 0; j < r / 2; ++j) {
    b[s][j] = a[s - 1][j + r / 2];
  }
  p[s].array = b[s];
  p[s].len = r / 2;
  for (i = 1; i < s; ++i) {
    for (j = 0; j < r; ++j) {
      idx = i * r + j - r / 2;
      b[i][j] = a[idx / r][idx % r];
    }
    p[i].array = b[i];
    p[i].len = r;
  }
  sort_columns(p, s + 1);
  for (j = r / 2; j < r; ++j) {
    a[0][j] = b[1][j - r / 2];
  }
  for (i = 1; i < s; ++i) {
    for (j = 0; j < r; ++j) {
      idx = i * r + j - r / 2;
      a[i][j] = b[idx / r + 1][idx % r];
    }
  }
  for (i = 0; i < s + 1; ++i) {
    free(b[i]);
  }
  free(b);
  free(p);
}

int
main(void)
{
  uint s, r, i, j, idx, n;
  num_t **a;
  num_t tmp;
  srand((unsigned)time(NULL));
  s = 5;
  r = 100;
  n = s * r;
  a = malloc(s * sizeof(num_t *));
  for (i = 0; i < s; ++i) {
    a[i] = malloc(r * sizeof(num_t));
    for (j = 0; j < r; ++j) {
      a[i][j] = i * r + j;
    }
  }
  for (i = 0; i < s; ++i) {
    for (j = 0; j < r; ++j) {
      idx = (unsigned)rand() % (n - (i * r + j)) + i * r + j;
      tmp = a[i][j];
      a[i][j] = a[idx / r][idx % r];
      a[idx / r][idx % r] = tmp;
    }
  }
  display_columns(a, s, r);
  printf("\nsorting...\n\n");
  columnsort(a, s, r);
  display_columns(a, s, r);
  for (i = 0; i < s; ++i) {
    free(a[i]);
  }
  free(a);
  return 0;
}
