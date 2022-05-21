import boolean as bool
import value as val
import operator as op

value_1 = val.Value(8)
value_2 = val.Value(5)
op_1 = op.Operator('>')
my_bool_1 = bool.Boolean(value_1, op_1, value_2)
value_1 = val.Value(3)
value_2 = val.Value(3)
op_2 = op.Operator('==')
my_bool_2 = bool.Boolean(value_1, op_2, value_2)

print(my_bool_1, my_bool_2)
print(my_bool_1.eval(), my_bool_2.eval())

val_1 = input("Bitte gebe Value 1 ein: ")
val_2 = input("Bitte gebe Value 2 ein: ")
oper = input("Bitte geben den Operator ein: ")

res = bool.Boolean(val_1, oper, val_2)

print(res)
print(res.eval())
