import html
import sqlite3


def generator(query, path):
    con = sqlite3.connect('./submodules/kbbi-data-source/kbbi.db')
    cur = con.cursor()
    cur.execute(query)
    dat = cur.fetchall()

    out = open(path, 'w')
    out.seek(0, 0)
    out.write(
        '#include <stdlib.h>\n'
        '#include <string.h>\n\n'
        '#include "kbbi_data.h"\n\n'
    )

    out.write('const int katakunci_size = '+str(len(dat))+';\n')
    out.write('char* katakunci[] = {')
    for row in dat:
        out.write('\"'+html.unescape(row[0])+'\",\n')
    out.write('};\n\n')

    out.write('const int artikata_size = '+str(len(dat))+';\n')
    out.write('char* artikata[] = {')
    for row in dat:
        out.write('\"'+(html.unescape(row[1])).replace('\"', '\\\"')+'\",\n')
    out.write('};\n\n')

    out.write(
        'Results* kbbi_data_init_result() {\n'
        '  Results* results = malloc(sizeof(struct results));\n'
        '  results->katakunci = NULL;\n'
        '  results->artikata = NULL;\n'
        '  results->next = NULL;\n'
        '  return results;\n'
        '}\n\n'
    )

    out.write(
        'void kbbi_data_free_result(Results* results){\n'
        '  if(results->next) {\n'
        '    kbbi_data_free_result(results->next);\n'
        '  }\n'
        '  free(results->katakunci);\n'
        '  free(results->artikata);\n'
        '  free(results);\n'
        '}\n\n'
    )

    out.write(
        'int kbbi_data_search(Results** result, int* result_count, const char* query, const int query_size){\n'
        '  if (*result != NULL)\n'
        '    kbbi_data_free_result(*result);\n'
        '  Results *head = NULL, *tracer = NULL;\n'
        '  *result_count = 0;\n'
        '  for (int i = 0; i < katakunci_size; i++){\n'
        '    if (strncmp(katakunci[i], query, query_size) == 0){\n'
        '      Results* temp = malloc(sizeof(struct results));\n'
        '      temp->next = NULL;\n'
        '      temp->katakunci = malloc(strlen(katakunci[i]) + 1);\n'
        '      strncpy(temp->katakunci, katakunci[i], strlen(katakunci[i]));\n'
        '      (temp->katakunci)[strlen(katakunci[i])] = \'\\0\';\n'
        '      temp->artikata = malloc(strlen(artikata[i]) + 1);\n'
        '      strncpy(temp->artikata, artikata[i], strlen(artikata[i]));\n'
        '      (temp->artikata)[strlen(artikata[i])] = \'\\0\';\n'
        '      if (head == NULL)\n'
        '        head = temp;\n'
        '      if (tracer == NULL) {\n'
        '        tracer = temp;\n'
        '      } else {\n'
        '        tracer->next = temp;\n'
        '        tracer = tracer->next;\n'
        '      }\n'
        '      (*result_count)++;'
        '    }\n'
        '  }\n'
        '  *result = head;\n'
        '  if((*result_count))\n'
        '    return 1;\n'
        '  return 0;'
        '}\n\n'
    )

    out.write(
        'int kbbi_data_count(){\n'
        '  return ' + str(len(dat)) + ';\n'
        '}\n\n'
    )

    cur.close()
    con.close()
    out.close()


def header(path):
    out = open(path, 'w')
    out.seek(0, 0)
    out.write(
        '#ifndef _KBBI_DATA_H\n'
        '#define _KBBI_DATA_H\n\n'
        'typedef struct results {\n'
        '  char* katakunci;\n'
        '  char* artikata;\n'
        '  struct results* next;\n'
        '} Results;\n\n'
        'Results* kbbi_data_init_result();\n\n'
        'void kbbi_data_free_result(Results* results);\n\n'
        'int kbbi_data_search(Results** results, int* result_count, const char* query, const int query_size);\n\n'
        'int kbbi_data_count();\n\n'
        '#endif'
    )
    out.close()


header('./out/kbbi_data.h')
generator('SELECT katakunci, artikata FROM datakata',
          './out/kbbi_data.c')
