#include <Python.h>

/**
 * print_python_string - prints Python string information
 * @p: Python object (string)
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    Py_ssize_t i;
    const char *str;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsUTF8(p);

    printf("  type: %s\n", (PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object"));
    printf("  length: %ld\n", length);
    printf("  value: %s\n", str);

    if (length > 10)
        length = 10;

    for (i = 0; i < length + 1; i++)
    {
        printf("%c", str[i]);
    }

    printf("\n");
}

