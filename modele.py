#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py
from peewee import *

baza_plik = 'dziennik.db'
############## genialny dzinnik wizjonera
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
