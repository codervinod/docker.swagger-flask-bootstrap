all:
	swagger_py_codegen --swagger-doc api.yaml app --ui --spec
	docker build -t webapp . 
