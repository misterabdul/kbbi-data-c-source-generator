#ifndef _KBBI_DATA_H
#define _KBBI_DATA_H

/* #define _KBBI_DATA_HIDE_INTERNALS */

typedef struct _results
{
  char* katakunci;
  char* artikata;
  struct _results* next;
} _Results;

_Results*
kbbi_data_init_result();

void
kbbi_data_free_result(_Results* results);

int
kbbi_data_search(_Results** results,
                 int* result_count,
                 const char* query,
                 const int query_size);

int
kbbi_data_count();

#endif
