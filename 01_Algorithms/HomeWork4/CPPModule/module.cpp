#include <Python.h>

long* two_mins(const long* arr, long size) {
	long a = arr[0];
	long b = arr[1];

	long* res = new long[2];

	if (a > b) {
		long temp = a;
		a = b;
		b = temp;
	}

	for (long i = 2; i < size; ++i) {
		if (arr[i] < a) {
			b = a;
			a = arr[i];
		}
		else if (arr[i] < b) {
			b = arr[i];
		}
	}

	res[0] = a;
	res[1] = b;

	return res;
}

PyObject* solution_cpp(PyObject *, PyObject* incoming) {

	long* a = new long[PyList_Size(incoming)];
	long* res = new long[2];
	for (long i = 0; i < PyList_Size(incoming); ++i) {
		PyObject* value = PyList_GetItem(incoming, i);
		a[i] = PyLong_AsLong(value);
	}

	res = two_mins(a, PyList_Size(incoming));

	PyObject* pyres = PyTuple_New(2);

	PyObject* num = PyLong_FromLong(res[0]);
	PyTuple_SET_ITEM(pyres, 0, num);

	num = PyLong_FromLong(res[1]);
	PyTuple_SET_ITEM(pyres, 1, num);

	return pyres;
}

static PyMethodDef twominscpp_methods[] = {
	{ "solution4", (PyCFunction)solution_cpp, METH_O, nullptr },
	{ nullptr, nullptr, 0, nullptr }
};

static PyModuleDef twominscpp_module = {
	PyModuleDef_HEAD_INIT,
	"twominscpp",                        // Module name to use with Python import statements
	"Provides some functions, but faster",  // Module description
	0,
	twominscpp_methods                   // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_twominscpp() {
	return PyModule_Create(&twominscpp_module);
}