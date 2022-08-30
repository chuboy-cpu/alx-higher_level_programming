#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int x;
	long int size = PyList_Size(p);
	PyListObject *item = (PyListObject *)p;

	printf("[*] Size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", item->allocated);
	for (x = 0; x < size; x++)
		printf("Element %i: %s\n", x, Py_Type(item->ob_item[x]->tp_name);
