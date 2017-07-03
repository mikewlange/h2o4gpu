import os
from ctypes import *
from h2oaiglm.types import *


ext = ".dylib" if os.uname()[0] == "Darwin" else ".so"
lib_path = os.path.join(os.path.dirname(__file__),"../../ch2oaiglm_cpu" + ext)

try:
	if not os.path.exists(lib_path):
		print("WARNING: Library " + lib_path + " doesn't exist.")
	h2oaiglmKMeansCPU = cdll.LoadLibrary(lib_path)

	h2oaiglmKMeansCPU.make_ptr_float_kmeans.argtypes = [c_int, c_int, c_size_t, c_size_t, c_int, c_int, c_int, c_int, c_int, c_int, c_float, c_float_p, c_int_p, c_void_pp]
	h2oaiglmKMeansCPU.make_ptr_float_kmeans.restype = c_int

	h2oaiglmKMeansCPU.make_ptr_double_kmeans.argtypes = [c_int, c_int, c_size_t, c_size_t, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_double_p, c_int_p, c_void_pp]
	h2oaiglmKMeansCPU.make_ptr_double_kmeans.restype = c_int
except:
	print('\nWarning: h2oaiglmKMeansCPU shared object (dynamic library) ' + lib_path + ' failed to load.')
	h2oaiglmKMeansCPU=None

