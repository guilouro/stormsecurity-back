### Como testar

#### Crie e ative um ambiente virtual
```
$ virtualenv stormsec
$ cd stormsec
$ source bin/activate
```
ou, utilizando [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
```
$ mkproject stormsec
```

#### Faça o clone do projeto
```
$ git clone https://github.com/guilouro/stormsecurity-back.git .
$ make install
```

#### Iniciar Server
```
$ make run
```