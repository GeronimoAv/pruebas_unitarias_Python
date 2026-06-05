# TESTING

(TODA LA DOCUMENTACION SE ENCUENTRA EN LA WIKI DEL REPOSITORIO)

## INTEGRANTES

Sadane Geronimo Miguel Santiago Acevedo Virgues

## estructura del proyecto

``` text
├── Dockerfile
├── README.md
├── prubas
├── pyproject.toml
├── scripts
├── src
│   └── domain
│       ├── model
│       │   ├── E_PRESTAMO.py
│       │   ├── E_TIPO_PRESTAMO.py
│       │   └── Q_PERSONA.py
│       └── service
│           └── Q_EVALUAR.py
└── tests
    ├── domain
    └── test_q_persona.py
```

## Indicaciones

- se crea primeramente la imagen de docker

``` cli
docker build -t mi_proyecto .
```

- corre el contenedor

```cli
docker run mi_proyecto pytest
```
