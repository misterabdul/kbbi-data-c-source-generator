#include <stdlib.h>
#include <string.h>

#include "kbbi_data.h"

#ifndef _KBBI_DATA_HIDE_INTERNALS
#define KBBI_INTERNAL_VISIBILITY
#else
#define KBBI_INTERNAL_VISIBILITY __attribute__((visibility("hidden")))
#endif

static const int katakunci_size = 0;
static char* katakunci[];

static const int artikata_size = 0;
static char* artikata[];

KBBI_INTERNAL_VISIBILITY _Results*
kbbi_data_init_result()
{
  _Results* results = malloc(sizeof(struct _results));
  results->katakunci = NULL;
  results->artikata = NULL;
  results->next = NULL;
  return results;
}

KBBI_INTERNAL_VISIBILITY void
kbbi_data_free_result(_Results* results)
{
  if (results->katakunci)
    free(results->katakunci);
  if (results->artikata)
    free(results->artikata);
  if (results->next)
    kbbi_data_free_result(results->next);
  if (results)
    free(results);
}

KBBI_INTERNAL_VISIBILITY int
kbbi_data_search(_Results** result,
                 int* result_count,
                 const char* query,
                 const int query_size)
{
  if (*result)
    kbbi_data_free_result(*result);
  _Results *head = NULL, *tracer = NULL;
  *result_count = 0;
  for (int i = 0; i < katakunci_size; i++) {
    if (strncmp(katakunci[i], query, query_size) == 0) {
      _Results* temp = malloc(sizeof(struct _results));
      temp->next = NULL;
      temp->katakunci = malloc(strlen(katakunci[i]) + 1);
      strncpy(temp->katakunci, katakunci[i], strlen(katakunci[i]));
      (temp->katakunci)[strlen(katakunci[i])] = '\0';
      temp->artikata = malloc(strlen(artikata[i]) + 1);
      strncpy(temp->artikata, artikata[i], strlen(artikata[i]));
      (temp->artikata)[strlen(artikata[i])] = '\0';
      if (head == NULL)
        head = temp;
      if (tracer == NULL) {
        tracer = temp;
      } else {
        tracer->next = temp;
        tracer = tracer->next;
      }
      (*result_count)++;
    }
  }
  *result = head;
  if ((*result_count))
    return 1;
  return 0;
}

KBBI_INTERNAL_VISIBILITY int
kbbi_data_count()
{
  return 0; /* tobe replaced */
}
