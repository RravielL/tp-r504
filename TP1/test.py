import pytest
import fonctions as f
def test_1():
	assert f.puissance(2,3)==8
	assert f.puissance(2,2)==4
	assert f.puissance(3 ,2)==9
def test_2():
	assert f.puissance(2,-2)==0.25
	assert f.puissance(10,-4)==0.0001
def test_3():
	assert f.puissance(2,2) ==4
	assert f.puissance(-2,2)==4
	assert f.puissance(2,0)==1 #marche pas
	assert f.puissance(-2,0)==-1
	assert f.puissance(0,0)==1
	assert f.puissance(0,3)==0
	assert f.puissance(0,-3)==0 #marche pas
