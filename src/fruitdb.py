#!/usr/bin/env python

from pydantic import BaseModel

class fruit(BaseModel):
    fruit_id: int
    fruit: str
    color: str

class fruitdb:
    fruits = {}

    def count(self) -> int:
        return len(self.fruits)

    def get_by_id(self, fruit_id: int) -> fruit:
        ret = self.fruits.get(fruit_id)
        if not ret:
            raise ValueError("!Item not found")
        return ret

    def get_all(self) -> list[fruit]:
        return self.fruits.values()

    def put(self, newitem: fruit):
        if self.fruits.get(newitem.fruit_id):
            raise ValueError("!Item already exists")
        self.fruits[newitem.fruit_id] = newitem

    def delete(self, fruit_id: int):
        if not self.fruits.get(fruit_id):
            raise ValueError("!Item not found")
        self.fruits.pop(fruit_id)

    def delete_all(self) -> None:
        self.fruits = {}
