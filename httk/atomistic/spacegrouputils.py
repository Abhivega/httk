# 
#    The high-throughput toolkit (httk)
#    Copyright (C) 2012-2015 Rickard Armiento
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from httk.core.fracvector import FracVector
from httk.core.mutablefracvector import MutableFracVector
from httk.core.basic import *

spacegroups = [
(1,1,"",("P1","A1","B1","C1","F1","I1"),"P 1","C1^1"), 
(2,1,"",("P-1","-A1","A-1","B-1","-B1","-C1","-C1","F-1","-F1","I-1","-I1"),"-P 1","Ci^1"), 
(3,1,"b",("P2:b","P121",),"P 2y","C2^1"), 
(3,2,"c",("P2:c","P112",),"P 2","C2^1"), 
(3,3,"a",("P2:a","P211",),"P 2x","C2^1"), 
(4,1,"b",("P21:b","P1211",),"P 2yb","C2^2"), 
(4,2,"c",("P21:c","P1121",),"P 2c","C2^2"), 
(4,3,"a",("P21:a","P2111",),"P 2xa","C2^2"), 
(5,1,"b1",("C2:b1","C121",),"C 2y","C2^3"), 
(5,2,"b2",("C2:b2","A121",),"A 2y","C2^3"), 
(5,3,"b3",("C2:b3","I121",),"I 2y","C2^3"), 
(5,4,"c1",("C2:c1","A112",),"A 2","C2^3"), 
(5,5,"c2",("C2:c2","B112","B2",),"B 2","C2^3"), 
(5,6,"c3",("C2:c3","I112",),"I 2","C2^3"), 
(5,7,"a1",("C2:a1","B211",),"B 2x","C2^3"), 
(5,8,"a2",("C2:a2","C211",),"C 2x","C2^3"), 
(5,9,"a3",("C2:a3","I211",),"I 2x","C2^3"), 
(6,1,"b",("Pm:b","P1m1",),"P -2y","Cs^1"), 
(6,2,"c",("Pm:c","P11m",),"P -2","Cs^1"), 
(6,3,"a",("Pm:a","Pm11",),"P -2x","Cs^1"), 
(7,1,"b1",("Pc:b1","P1c1",),"P -2yc","Cs^2"), 
(7,2,"b2",("Pc:b2","P1n1",),"P -2yac","Cs^2"), 
(7,3,"b3",("Pc:b3","P1a1",),"P -2ya","Cs^2"), 
(7,4,"c1",("Pc:c1","P11a",),"P -2a","Cs^2"), 
(7,5,"c2",("Pc:c2","P11n",),"P -2ab","Cs^2"), 
(7,6,"c3",("Pc:c3","P11b","Pb",),"P -2b","Cs^2"), 
(7,7,"a1",("Pc:a1","Pb11",),"P -2xb","Cs^2"), 
(7,8,"a2",("Pc:a2","Pn11",),"P -2xbc","Cs^2"), 
(7,9,"a3",("Pc:a3","Pc11",),"P -2xc","Cs^2"), 
(8,1,"b1",("Cm:b1","C1m1",),"C -2y","Cs^3"), 
(8,2,"b2",("Cm:b2","A1m1",),"A -2y","Cs^3"), 
(8,3,"b3",("Cm:b3","I1m1",),"I -2y","Cs^3"), 
(8,4,"c1",("Cm:c1","A11m",),"A -2","Cs^3"), 
(8,5,"c2",("Cm:c2","B11m","Bm",),"B -2","Cs^3"), 
(8,6,"c3",("Cm:c3","I11m",),"I -2","Cs^3"), 
(8,7,"a1",("Cm:a1","Bm11",),"B -2x","Cs^3"), 
(8,8,"a2",("Cm:a2","Cm11",),"C -2x","Cs^3"), 
(8,9,"a3",("Cm:a3","Im11",),"I -2x","Cs^3"), 
(9,1,"b1",("Cc:b1","C1c1",),"C -2yc","Cs^4"), 
(9,2,"b2",("Cc:b2","A1n1",),"A -2yac","Cs^4"), 
(9,3,"b3",("Cc:b3","I1a1",),"I -2ya","Cs^4"), 
(9,4,"-b1",("Cc:-b1","A1a1",),"A -2ya","Cs^4"), 
(9,5,"-b2",("Cc:-b2","C1n1",),"C -2ybc","Cs^4"), 
(9,6,"-b3",("Cc:-b3","I1c1",),"I -2yc","Cs^4"), 
(9,7,"c1",("Cc:c1","A11a",),"A -2a","Cs^4"), 
(9,8,"c2",("Cc:c2","B11n",),"B -2bc","Cs^4"), 
(9,9,"c3",("Cc:c3","I11b",),"I -2b","Cs^4"), 
(9,10,"-c1",("Cc:-c1","B11b","Bb",),"B -2b","Cs^4"), 
(9,11,"-c2",("Cc:-c2","A11n",),"A -2ac","Cs^4"), 
(9,12,"-c3",("Cc:-c3","I11a",),"I -2a","Cs^4"), 
(9,13,"a1",("Cc:a1","Bb11",),"B -2xb","Cs^4"), 
(9,14,"a2",("Cc:a2","Cn11",),"C -2xbc","Cs^4"), 
(9,15,"a3",("Cc:a3","Ic11",),"I -2xc","Cs^4"), 
(9,16,"-a1",("Cc:-a1","Cc11",),"C -2xc","Cs^4"), 
(9,17,"-a2",("Cc:-a2","Bn11",),"B -2xbc","Cs^4"), 
(9,18,"-a3",("Cc:-a3","Ib11",),"I -2xb","Cs^4"), 
(10,1,"b",("P2/m:b","P12/m1",),"-P 2y","C2h^1"), 
(10,2,"c",("P2/m:c","P112/m",),"-P 2","C2h^1"), 
(10,3,"a",("P2/m:a","P2/m11",),"-P 2x","C2h^1"), 
(11,1,"b",("P21/m:b","P121/m1",),"-P 2yb","C2h^2"), 
(11,2,"c",("P21/m:c","P1121/m",),"-P 2c","C2h^2"), 
(11,3,"a",("P21/m:a","P21/m11",),"-P 2xa","C2h^2"), 
(12,1,"b1",("C2/m:b1","C12/m1",),"-C 2y","C2h^3"), 
(12,2,"b2",("C2/m:b2","A12/m1",),"-A 2y","C2h^3"), 
(12,3,"b3",("C2/m:b3","I12/m1",),"-I 2y","C2h^3"), 
(12,4,"c1",("C2/m:c1","A112/m",),"-A 2","C2h^3"), 
(12,5,"c2",("C2/m:c2","B112/m","B2/m",),"-B 2","C2h^3"), 
(12,6,"c3",("C2/m:c3","I112/m",),"-I 2","C2h^3"), 
(12,7,"a1",("C2/m:a1","B2/m11",),"-B 2x","C2h^3"), 
(12,8,"a2",("C2/m:a2","C2/m11",),"-C 2x","C2h^3"), 
(12,9,"a3",("C2/m:a3","I2/m11",),"-I 2x","C2h^3"), 
(13,1,"b1",("P2/c:b1","P12/c1",),"-P 2yc","C2h^4"), 
(13,2,"b2",("P2/c:b2","P12/n1",),"-P 2yac","C2h^4"), 
(13,3,"b3",("P2/c:b3","P12/a1",),"-P 2ya","C2h^4"), 
(13,4,"c1",("P2/c:c1","P112/a",),"-P 2a","C2h^4"), 
(13,5,"c2",("P2/c:c2","P112/n",),"-P 2ab","C2h^4"), 
(13,6,"c3",("P2/c:c3","P112/b","P2/b",),"-P 2b","C2h^4"), 
(13,7,"a1",("P2/c:a1","P2/b11",),"-P 2xb","C2h^4"), 
(13,8,"a2",("P2/c:a2","P2/n11",),"-P 2xbc","C2h^4"), 
(13,9,"a3",("P2/c:a3","P2/c11",),"-P 2xc","C2h^4"), 
(14,1,"b1",("P21/c:b1","P121/c1",),"-P 2ybc","C2h^5"), 
(14,2,"b2",("P21/c:b2","P121/n1",),"-P 2yn","C2h^5"), 
(14,3,"b3",("P21/c:b3","P121/a1",),"-P 2yab","C2h^5"), 
(14,4,"c1",("P21/c:c1","P1121/a",),"-P 2ac","C2h^5"), 
(14,5,"c2",("P21/c:c2","P1121/n",),"-P 2n","C2h^5"), 
(14,6,"c3",("P21/c:c3","P1121/b","P21/b",),"-P 2bc","C2h^5"), 
(14,7,"a1",("P21/c:a1","P21/b11",),"-P 2xab","C2h^5"), 
(14,8,"a2",("P21/c:a2","P21/n11",),"-P 2xn","C2h^5"), 
(14,9,"a3",("P21/c:a3","P21/c11",),"-P 2xac","C2h^5"), 
(15,1,"b1",("C2/c:b1","C12/c1",),"-C 2yc","C2h^6"), 
(15,2,"b2",("C2/c:b2","A12/n1",),"-A 2yac","C2h^6"), 
(15,3,"b3",("C2/c:b3","I12/a1",),"-I 2ya","C2h^6"), 
(15,4,"-b1",("C2/c:-b1","A12/a1",),"-A 2ya","C2h^6"), 
(15,5,"-b2",("C2/c:-b2","C12/n1",),"-C 2ybc","C2h^6"), 
(15,6,"-b3",("C2/c:-b3","I12/c1",),"-I 2yc","C2h^6"), 
(15,7,"c1",("C2/c:c1","A112/a",),"-A 2a","C2h^6"), 
(15,8,"c2",("C2/c:c2","B112/n",),"-B 2bc","C2h^6"), 
(15,9,"c3",("C2/c:c3","I112/b",),"-I 2b","C2h^6"), 
(15,10,"-c1",("C2/c:-c1","B112/b","B2/b",),"-B 2b","C2h^6"), 
(15,11,"-c2",("C2/c:-c2","A112/n",),"-A 2ac","C2h^6"), 
(15,12,"-c3",("C2/c:-c3","I112/a",),"-I 2a","C2h^6"), 
(15,13,"a1",("C2/c:a1","B2/b11",),"-B 2xb","C2h^6"), 
(15,14,"a2",("C2/c:a2","C2/n11",),"-C 2xbc","C2h^6"), 
(15,15,"a3",("C2/c:a3","I2/c11",),"-I 2xc","C2h^6"), 
(15,16,"-a1",("C2/c:-a1","C2/c11",),"-C 2xc","C2h^6"), 
(15,17,"-a2",("C2/c:-a2","B2/n11",),"-B 2xbc","C2h^6"), 
(15,18,"-a3",("C2/c:-a3","I2/b11",),"-I 2xb","C2h^6"), 
(16,1,"",("P222",),"P 2 2","D2^1"), 
(17,1,"",("P2221",),"P 2c 2","D2^2"), 
(17,2,"cab",("P2122",),"P 2a 2a","D2^2"), 
(17,3,"bca",("P2212",),"P 2 2b","D2^2"), 
(18,1,"",("P21212",),"P 2 2ab","D2^3"), 
(18,2,"cab",("P22121",),"P 2bc 2","D2^3"), 
(18,3,"bca",("P21221",),"P 2ac 2ac","D2^3"), 
(19,1,"",("P212121",),"P 2ac 2ab","D2^4"), 
(20,1,"",("C2221",),"C 2c 2","D2^5"), 
(20,2,"cab",("A2122",),"A 2a 2a","D2^5"), 
(20,3,"bca",("B2212",),"B 2 2b","D2^5"), 
(21,1,"",("C222",),"C 2 2","D2^6"), 
(21,2,"cab",("A222",),"A 2 2","D2^6"), 
(21,3,"bca",("B222",),"B 2 2","D2^6"), 
(22,1,"",("F222",),"F 2 2","D2^7"), 
(23,1,"",("I222",),"I 2 2","D2^8"), 
(24,1,"",("I212121",),"I 2b 2c","D2^9"), 
(25,1,"",("Pmm2",),"P 2 -2","C2v^1"), 
(25,2,"cab",("P2mm",),"P -2 2","C2v^1"), 
(25,3,"bca",("Pm2m",),"P -2 -2","C2v^1"), 
(26,1,"",("Pmc21",),"P 2c -2","C2v^2"), 
(26,2,"ba-c",("Pcm21",),"P 2c -2c","C2v^2"), 
(26,3,"cab",("P21ma",),"P -2a 2a","C2v^2"), 
(26,4,"-cba",("P21am",),"P -2 2a","C2v^2"), 
(26,5,"bca",("Pb21m",),"P -2 -2b","C2v^2"), 
(26,6,"a-cb",("Pm21b",),"P -2b -2","C2v^2"), 
(27,1,"",("Pcc2",),"P 2 -2c","C2v^3"), 
(27,2,"cab",("P2aa",),"P -2a 2","C2v^3"), 
(27,3,"bca",("Pb2b",),"P -2b -2b","C2v^3"), 
(28,1,"",("Pma2",),"P 2 -2a","C2v^4"), 
(28,2,"ba-c",("Pbm2",),"P 2 -2b","C2v^4"), 
(28,3,"cab",("P2mb",),"P -2b 2","C2v^4"), 
(28,4,"-cba",("P2cm",),"P -2c 2","C2v^4"), 
(28,5,"bca",("Pc2m",),"P -2c -2c","C2v^4"), 
(28,6,"a-cb",("Pm2a",),"P -2a -2a","C2v^4"), 
(29,1,"",("Pca21",),"P 2c -2ac","C2v^5"), 
(29,2,"ba-c",("Pbc21",),"P 2c -2b","C2v^5"), 
(29,3,"cab",("P21ab",),"P -2b 2a","C2v^5"), 
(29,4,"-cba",("P21ca",),"P -2ac 2a","C2v^5"), 
(29,5,"bca",("Pc21b",),"P -2bc -2c","C2v^5"), 
(29,6,"a-cb",("Pb21a",),"P -2a -2ab","C2v^5"), 
(30,1,"",("Pnc2",),"P 2 -2bc","C2v^6"), 
(30,2,"ba-c",("Pcn2",),"P 2 -2ac","C2v^6"), 
(30,3,"cab",("P2na",),"P -2ac 2","C2v^6"), 
(30,4,"-cba",("P2an",),"P -2ab 2","C2v^6"), 
(30,5,"bca",("Pb2n",),"P -2ab -2ab","C2v^6"), 
(30,6,"a-cb",("Pn2b",),"P -2bc -2bc","C2v^6"), 
(31,1,"",("Pmn21",),"P 2ac -2","C2v^7"), 
(31,2,"ba-c",("Pnm21",),"P 2bc -2bc","C2v^7"), 
(31,3,"cab",("P21mn",),"P -2ab 2ab","C2v^7"), 
(31,4,"-cba",("P21nm",),"P -2 2ac","C2v^7"), 
(31,5,"bca",("Pn21m",),"P -2 -2bc","C2v^7"), 
(31,6,"a-cb",("Pm21n",),"P -2ab -2","C2v^7"), 
(32,1,"",("Pba2",),"P 2 -2ab","C2v^8"), 
(32,2,"cab",("P2cb",),"P -2bc 2","C2v^8"), 
(32,3,"bca",("Pc2a",),"P -2ac -2ac","C2v^8"), 
(33,1,"",("Pna21",),"P 2c -2n","C2v^9"), 
(33,2,"ba-c",("Pbn21",),"P 2c -2ab","C2v^9"), 
(33,3,"cab",("P21nb",),"P -2bc 2a","C2v^9"), 
(33,4,"-cba",("P21cn",),"P -2n 2a","C2v^9"), 
(33,5,"bca",("Pc21n",),"P -2n -2ac","C2v^9"), 
(33,6,"a-cb",("Pn21a",),"P -2ac -2n","C2v^9"), 
(34,1,"",("Pnn2",),"P 2 -2n","C2v^10"), 
(34,2,"cab",("P2nn",),"P -2n 2","C2v^10"), 
(34,3,"bca",("Pn2n",),"P -2n -2n","C2v^10"), 
(35,1,"",("Cmm2",),"C 2 -2","C2v^11"), 
(35,2,"cab",("A2mm",),"A -2 2","C2v^11"), 
(35,3,"bca",("Bm2m",),"B -2 -2","C2v^11"), 
(36,1,"",("Cmc21",),"C 2c -2","C2v^12"), 
(36,2,"ba-c",("Ccm21",),"C 2c -2c","C2v^12"), 
(36,3,"cab",("A21ma",),"A -2a 2a","C2v^12"), 
(36,4,"-cba",("A21am",),"A -2 2a","C2v^12"), 
(36,5,"bca",("Bb21m",),"B -2 -2b","C2v^12"), 
(36,6,"a-cb",("Bm21b",),"B -2b -2","C2v^12"), 
(37,1,"",("Ccc2",),"C 2 -2c","C2v^13"), 
(37,2,"cab",("A2aa",),"A -2a 2","C2v^13"), 
(37,3,"bca",("Bb2b",),"B -2b -2b","C2v^13"), 
(38,1,"",("Amm2",),"A 2 -2","C2v^14"), 
(38,2,"ba-c",("Bmm2",),"B 2 -2","C2v^14"), 
(38,3,"cab",("B2mm",),"B -2 2","C2v^14"), 
(38,4,"-cba",("C2mm",),"C -2 2","C2v^14"), 
(38,5,"bca",("Cm2m",),"C -2 -2","C2v^14"), 
(38,6,"a-cb",("Am2m",),"A -2 -2","C2v^14"), 
(39,1,"",("Abm2",),"A 2 -2c","C2v^15"), 
(39,2,"ba-c",("Bma2",),"B 2 -2c","C2v^15"), 
(39,3,"cab",("B2cm",),"B -2c 2","C2v^15"), 
(39,4,"-cba",("C2mb",),"C -2b 2","C2v^15"), 
(39,5,"bca",("Cm2a",),"C -2b -2b","C2v^15"), 
(39,6,"a-cb",("Ac2m",),"A -2c -2c","C2v^15"), 
(40,1,"",("Ama2",),"A 2 -2a","C2v^16"), 
(40,2,"ba-c",("Bbm2",),"B 2 -2b","C2v^16"), 
(40,3,"cab",("B2mb",),"B -2b 2","C2v^16"), 
(40,4,"-cba",("C2cm",),"C -2c 2","C2v^16"), 
(40,5,"bca",("Cc2m",),"C -2c -2c","C2v^16"), 
(40,6,"a-cb",("Am2a",),"A -2a -2a","C2v^16"), 
(41,1,"",("Aba2",),"A 2 -2ac","C2v^17"), 
(41,2,"ba-c",("Bba2",),"B 2 -2bc","C2v^17"), 
(41,3,"cab",("B2cb",),"B -2bc 2","C2v^17"), 
(41,4,"-cba",("C2cb",),"C -2bc 2","C2v^17"), 
(41,5,"bca",("Cc2a",),"C -2bc -2bc","C2v^17"), 
(41,6,"a-cb",("Ac2a",),"A -2ac -2ac","C2v^17"), 
(42,1,"",("Fmm2",),"F 2 -2","C2v^18"), 
(42,2,"cab",("F2mm",),"F -2 2","C2v^18"), 
(42,3,"bca",("Fm2m",),"F -2 -2","C2v^18"), 
(43,1,"",("Fdd2",),"F 2 -2d","C2v^19"), 
(43,2,"cab",("F2dd",),"F -2d 2","C2v^19"), 
(43,3,"bca",("Fd2d",),"F -2d -2d","C2v^19"), 
(44,1,"",("Imm2",),"I 2 -2","C2v^20"), 
(44,2,"cab",("I2mm",),"I -2 2","C2v^20"), 
(44,3,"bca",("Im2m",),"I -2 -2","C2v^20"), 
(45,1,"",("Iba2",),"I 2 -2c","C2v^21"), 
(45,2,"cab",("I2cb",),"I -2a 2","C2v^21"), 
(45,3,"bca",("Ic2a",),"I -2b -2b","C2v^21"), 
(46,1,"",("Ima2",),"I 2 -2a","C2v^22"), 
(46,2,"ba-c",("Ibm2",),"I 2 -2b","C2v^22"), 
(46,3,"cab",("I2mb",),"I -2b 2","C2v^22"), 
(46,4,"-cba",("I2cm",),"I -2c 2","C2v^22"), 
(46,5,"bca",("Ic2m",),"I -2c -2c","C2v^22"), 
(46,6,"a-cb",("Im2a",),"I -2a -2a","C2v^22"), 
(47,1,"",("Pmmm",),"-P 2 2","D2h^1"), 
(48,1,"1",("Pnnn:1",),"P 2 2 -1n","D2h^2"), 
(48,2,"2",("Pnnn:2",),"-P 2ab 2bc","D2h^2"), 
(49,1,"",("Pccm",),"-P 2 2c","D2h^3"), 
(49,2,"cab",("Pmaa",),"-P 2a 2","D2h^3"), 
(49,3,"bca",("Pbmb",),"-P 2b 2b","D2h^3"), 
(50,1,"1",("Pban:1",),"P 2 2 -1ab","D2h^4"), 
(50,2,"2",("Pban:2",),"-P 2ab 2b","D2h^4"), 
(50,3,"1cab",("Pncb:1",),"P 2 2 -1bc","D2h^4"), 
(50,4,"2cab",("Pncb:2",),"-P 2b 2bc","D2h^4"), 
(50,5,"1bca",("Pcna:1",),"P 2 2 -1ac","D2h^4"), 
(50,6,"2bca",("Pcna:2",),"-P 2a 2c","D2h^4"), 
(51,1,"",("Pmma",),"-P 2a 2a","D2h^5"), 
(51,2,"ba-c",("Pmmb",),"-P 2b 2","D2h^5"), 
(51,3,"cab",("Pbmm",),"-P 2 2b","D2h^5"), 
(51,4,"-cba",("Pcmm",),"-P 2c 2c","D2h^5"), 
(51,5,"bca",("Pmcm",),"-P 2c 2","D2h^5"), 
(51,6,"a-cb",("Pmam",),"-P 2 2a","D2h^5"), 
(52,1,"",("Pnna",),"-P 2a 2bc","D2h^6"), 
(52,2,"ba-c",("Pnnb",),"-P 2b 2n","D2h^6"), 
(52,3,"cab",("Pbnn",),"-P 2n 2b","D2h^6"), 
(52,4,"-cba",("Pcnn",),"-P 2ab 2c","D2h^6"), 
(52,5,"bca",("Pncn",),"-P 2ab 2n","D2h^6"), 
(52,6,"a-cb",("Pnan",),"-P 2n 2bc","D2h^6"), 
(53,1,"",("Pmna",),"-P 2ac 2","D2h^7"), 
(53,2,"ba-c",("Pnmb",),"-P 2bc 2bc","D2h^7"), 
(53,3,"cab",("Pbmn",),"-P 2ab 2ab","D2h^7"), 
(53,4,"-cba",("Pcnm",),"-P 2 2ac","D2h^7"), 
(53,5,"bca",("Pncm",),"-P 2 2bc","D2h^7"), 
(53,6,"a-cb",("Pman",),"-P 2ab 2","D2h^7"), 
(54,1,"",("Pcca",),"-P 2a 2ac","D2h^8"), 
(54,2,"ba-c",("Pccb",),"-P 2b 2c","D2h^8"), 
(54,3,"cab",("Pbaa",),"-P 2a 2b","D2h^8"), 
(54,4,"-cba",("Pcaa",),"-P 2ac 2c","D2h^8"), 
(54,5,"bca",("Pbcb",),"-P 2bc 2b","D2h^8"), 
(54,6,"a-cb",("Pbab",),"-P 2b 2ab","D2h^8"), 
(55,1,"",("Pbam",),"-P 2 2ab","D2h^9"), 
(55,2,"cab",("Pmcb",),"-P 2bc 2","D2h^9"), 
(55,3,"bca",("Pcma",),"-P 2ac 2ac","D2h^9"), 
(56,1,"",("Pccn",),"-P 2ab 2ac","D2h^10"), 
(56,2,"cab",("Pnaa",),"-P 2ac 2bc","D2h^10"), 
(56,3,"bca",("Pbnb",),"-P 2bc 2ab","D2h^10"), 
(57,1,"",("Pbcm",),"-P 2c 2b","D2h^11"), 
(57,2,"ba-c",("Pcam",),"-P 2c 2ac","D2h^11"), 
(57,3,"cab",("Pmca",),"-P 2ac 2a","D2h^11"), 
(57,4,"-cba",("Pmab",),"-P 2b 2a","D2h^11"), 
(57,5,"bca",("Pbma",),"-P 2a 2ab","D2h^11"), 
(57,6,"a-cb",("Pcmb",),"-P 2bc 2c","D2h^11"), 
(58,1,"",("Pnnm",),"-P 2 2n","D2h^12"), 
(58,2,"cab",("Pmnn",),"-P 2n 2","D2h^12"), 
(58,3,"bca",("Pnmn",),"-P 2n 2n","D2h^12"), 
(59,1,"1",("Pmmn:1",),"P 2 2ab -1ab","D2h^13"), 
(59,2,"2",("Pmmn:2",),"-P 2ab 2a","D2h^13"), 
(59,3,"1cab",("Pnmm:1",),"P 2bc 2 -1bc","D2h^13"), 
(59,4,"2cab",("Pnmm:2",),"-P 2c 2bc","D2h^13"), 
(59,5,"1bca",("Pmnm:1",),"P 2ac 2ac -1ac","D2h^13"), 
(59,6,"2bca",("Pmnm:2",),"-P 2c 2a","D2h^13"), 
(60,1,"",("Pbcn",),"-P 2n 2ab","D2h^14"), 
(60,2,"ba-c",("Pcan",),"-P 2n 2c","D2h^14"), 
(60,3,"cab",("Pnca",),"-P 2a 2n","D2h^14"), 
(60,4,"-cba",("Pnab",),"-P 2bc 2n","D2h^14"), 
(60,5,"bca",("Pbna",),"-P 2ac 2b","D2h^14"), 
(60,6,"a-cb",("Pcnb",),"-P 2b 2ac","D2h^14"), 
(61,1,"",("Pbca",),"-P 2ac 2ab","D2h^15"), 
(61,2,"ba-c",("Pcab",),"-P 2bc 2ac","D2h^15"), 
(62,1,"",("Pnma",),"-P 2ac 2n","D2h^16"), 
(62,2,"ba-c",("Pmnb",),"-P 2bc 2a","D2h^16"), 
(62,3,"cab",("Pbnm",),"-P 2c 2ab","D2h^16"), 
(62,4,"-cba",("Pcmn",),"-P 2n 2ac","D2h^16"), 
(62,5,"bca",("Pmcn",),"-P 2n 2a","D2h^16"), 
(62,6,"a-cb",("Pnam",),"-P 2c 2n","D2h^16"), 
(63,1,"",("Cmcm",),"-C 2c 2","D2h^17"), 
(63,2,"ba-c",("Ccmm",),"-C 2c 2c","D2h^17"), 
(63,3,"cab",("Amma",),"-A 2a 2a","D2h^17"), 
(63,4,"-cba",("Amam",),"-A 2 2a","D2h^17"), 
(63,5,"bca",("Bbmm",),"-B 2 2b","D2h^17"), 
(63,6,"a-cb",("Bmmb",),"-B 2b 2","D2h^17"), 
(64,1,"",("Cmca",),"-C 2bc 2","D2h^18"), 
(64,2,"ba-c",("Ccmb",),"-C 2bc 2bc","D2h^18"), 
(64,3,"cab",("Abma",),"-A 2ac 2ac","D2h^18"), 
(64,4,"-cba",("Acam",),"-A 2 2ac","D2h^18"), 
(64,5,"bca",("Bbcm",),"-B 2 2bc","D2h^18"), 
(64,6,"a-cb",("Bmab",),"-B 2bc 2","D2h^18"), 
(65,1,"",("Cmmm",),"-C 2 2","D2h^19"), 
(65,2,"cab",("Ammm",),"-A 2 2","D2h^19"), 
(65,3,"bca",("Bmmm",),"-B 2 2","D2h^19"), 
(66,1,"",("Cccm",),"-C 2 2c","D2h^20"), 
(66,2,"cab",("Amaa",),"-A 2a 2","D2h^20"), 
(66,3,"bca",("Bbmb",),"-B 2b 2b","D2h^20"), 
(67,1,"",("Cmma",),"-C 2b 2","D2h^21"), 
(67,2,"ba-c",("Cmmb",),"-C 2b 2b","D2h^21"), 
(67,3,"cab",("Abmm",),"-A 2c 2c","D2h^21"), 
(67,4,"-cba",("Acmm",),"-A 2 2c","D2h^21"), 
(67,5,"bca",("Bmcm",),"-B 2 2c","D2h^21"), 
(67,6,"a-cb",("Bmam",),"-B 2c 2","D2h^21"), 
(68,1,"1",("Ccca:1",),"C 2 2 -1bc","D2h^22"), 
(68,2,"2",("Ccca:2",),"-C 2b 2bc","D2h^22"), 
(68,3,"1ba-c",("Cccb:1",),"C 2 2 -1bc","D2h^22"), 
(68,4,"2ba-c",("Cccb:2",),"-C 2b 2c","D2h^22"), 
(68,5,"1cab",("Abaa:1",),"A 2 2 -1ac","D2h^22"), 
(68,6,"2cab",("Abaa:2",),"-A 2a 2c","D2h^22"), 
(68,7,"1-cba",("Acaa:1",),"A 2 2 -1ac","D2h^22"), 
(68,8,"2-cba",("Acaa:2",),"-A 2ac 2c","D2h^22"), 
(68,9,"1bca",("Bbcb:1",),"B 2 2 -1bc","D2h^22"), 
(68,10,"2bca",("Bbcb:2",),"-B 2bc 2b","D2h^22"), 
(68,11,"1a-cb",("Bbab:1",),"B 2 2 -1bc","D2h^22"), 
(68,12,"2a-cb",("Bbab:2",),"-B 2b 2bc","D2h^22"), 
(69,1,"",("Fmmm",),"-F 2 2","D2h^23"), 
(70,1,"1",("Fddd:1",),"F 2 2 -1d","D2h^24"), # What is "-F 2 2 -1d"?! It comes out of cif2cell
(70,2,"2",("Fddd:2",),"-F 2uv 2vw","D2h^24"), 
(71,1,"",("Immm",),"-I 2 2","D2h^25"), 
(72,1,"",("Ibam",),"-I 2 2c","D2h^26"), 
(72,2,"cab",("Imcb",),"-I 2a 2","D2h^26"), 
(72,3,"bca",("Icma",),"-I 2b 2b","D2h^26"), 
(73,1,"",("Ibca",),"-I 2b 2c","D2h^27"), 
(73,2,"ba-c",("Icab",),"-I 2a 2b","D2h^27"), 
(74,1,"",("Imma",),"-I 2b 2","D2h^28"), 
(74,2,"ba-c",("Immb",),"-I 2a 2a","D2h^28"), 
(74,3,"cab",("Ibmm",),"-I 2c 2c","D2h^28"), 
(74,4,"-cba",("Icmm",),"-I 2 2b","D2h^28"), 
(74,5,"bca",("Imcm",),"-I 2 2a","D2h^28"), 
(74,6,"a-cb",("Imam",),"-I 2c 2","D2h^28"), 
(75,1,"",("P4",),"P 4","C4^1"), 
(76,1,"",("P41",),"P 4w","C4^2"), 
(77,1,"",("P42",),"P 4c","C4^3"), 
(78,1,"",("P43",),"P 4cw","C4^4"), 
(79,1,"",("I4",),"I 4","C4^5"), 
(80,1,"",("I41",),"I 4bw","C4^6"), 
(81,1,"",("P-4",),"P -4","S4^1"), 
(82,1,"",("I-4",),"I -4","S4^2"), 
(83,1,"",("P4/m",),"-P 4","C4h^1"), 
(84,1,"",("P42/m",),"-P 4c","C4h^2"), 
(85,1,"1",("P4/n:1",),"P 4ab -1ab","C4h^3"), 
(85,2,"2",("P4/n:2",),"-P 4a","C4h^3"), 
(86,1,"1",("P42/n:1",),"P 4n -1n","C4h^4"), 
(86,2,"2",("P42/n:2",),"-P 4bc","C4h^4"), 
(87,1,"",("I4/m",),"-I 4","C4h^5"), 
(88,1,"1",("I41/a:1",),"I 4bw -1bw","C4h^6"), 
(88,2,"2",("I41/a:2",),"-I 4ad","C4h^6"), 
(89,1,"",("P422",),"P 4 2","D4^1"), 
(90,1,"",("P4212",),"P 4ab 2ab","D4^2"), 
(91,1,"",("P4122",),"P 4w 2c","D4^3"), 
(92,1,"",("P41212",),"P 4abw 2nw","D4^4"), 
(93,1,"",("P4222",),"P 4c 2","D4^5"), 
(94,1,"",("P42212",),"P 4n 2n","D4^6"), 
(95,1,"",("P4322",),"P 4cw 2c","D4^7"), 
(96,1,"",("P43212",),"P 4nw 2abw","D4^8"), 
(97,1,"",("I422",),"I 4 2","D4^9"), 
(98,1,"",("I4122",),"I 4bw 2bw","D4^10"), 
(99,1,"",("P4mm",),"P 4 -2","C4v^1"), 
(100,1,"",("P4bm",),"P 4 -2ab","C4v^2"), 
(101,1,"",("P42cm",),"P 4c -2c","C4v^3"), 
(102,1,"",("P42nm",),"P 4n -2n","C4v^4"), 
(103,1,"",("P4cc",),"P 4 -2c","C4v^5"), 
(104,1,"",("P4nc",),"P 4 -2n","C4v^6"), 
(105,1,"",("P42mc",),"P 4c -2","C4v^7"), 
(106,1,"",("P42bc",),"P 4c -2ab","C4v^8"), 
(107,1,"",("I4mm",),"I 4 -2","C4v^9"), 
(108,1,"",("I4cm",),"I 4 -2c","C4v^10"), 
(109,1,"",("I41md",),"I 4bw -2","C4v^11"), 
(110,1,"",("I41cd",),"I 4bw -2c","C4v^12"), 
(111,1,"",("P-42m",),"P -4 2","D2d^1"), 
(112,1,"",("P-42c",),"P -4 2c","D2d^2"), 
(113,1,"",("P-421m",),"P -4 2ab","D2d^3"), 
(114,1,"",("P-421c",),"P -4 2n","D2d^4"), 
(115,1,"",("P-4m2",),"P -4 -2","D2d^5"), 
(116,1,"",("P-4c2",),"P -4 -2c","D2d^6"), 
(117,1,"",("P-4b2",),"P -4 -2ab","D2d^7"), 
(118,1,"",("P-4n2",),"P -4 -2n","D2d^8"), 
(119,1,"",("I-4m2",),"I -4 -2","D2d^9"), 
(120,1,"",("I-4c2",),"I -4 -2c","D2d^10"), 
(121,1,"",("I-42m",),"I -4 2","D2d^11"), 
(122,1,"",("I-42d",),"I -4 2bw","D2d^12"), 
(123,1,"",("P4/mmm",),"-P 4 2","D4h^1"), 
(124,1,"",("P4/mcc",),"-P 4 2c","D4h^2"), 
(125,1,"1",("P4/nbm:1",),"P 4 2 -1ab","D4h^3"), 
(125,2,"2",("P4/nbm:2",),"-P 4a 2b","D4h^3"), 
(126,1,"1",("P4/nnc:1",),"P 4 2 -1n","D4h^4"), 
(126,2,"2",("P4/nnc:2",),"-P 4a 2bc","D4h^4"), 
(127,1,"",("P4/mbm",),"-P 4 2ab","D4h^5"), 
(128,1,"",("P4/mnc",),"-P 4 2n","D4h^6"), 
(129,1,"1",("P4/nmm:1",),"P 4ab 2ab -1ab","D4h^7"), 
(129,2,"2",("P4/nmm:2",),"-P 4a 2a","D4h^7"), 
(130,1,"1",("P4/ncc:1",),"P 4ab 2n -1ab","D4h^8"), 
(130,2,"2",("P4/ncc:2",),"-P 4a 2ac","D4h^8"), 
(131,1,"",("P42/mmc",),"-P 4c 2","D4h^9"), 
(132,1,"",("P42/mcm",),"-P 4c 2c","D4h^10"), 
(133,1,"1",("P42/nbc:1",),"P 4n 2c -1n","D4h^11"), 
(133,2,"2",("P42/nbc:2",),"-P 4ac 2b","D4h^11"), 
(134,1,"1",("P42/nnm:1",),"P 4n 2 -1n","D4h^12"), 
(134,2,"2",("P42/nnm:2",),"-P 4ac 2bc","D4h^12"), 
(135,1,"",("P42/mbc",),"-P 4c 2ab","D4h^13"), 
(136,1,"",("P42/mnm",),"-P 4n 2n","D4h^14"), 
(137,1,"1",("P42/nmc:1",),"P 4n 2n -1n","D4h^15"), 
(137,2,"2",("P42/nmc:2",),"-P 4ac 2a","D4h^15"), 
(138,1,"1",("P42/ncm:1",),"P 4n 2ab -1n","D4h^16"), 
(138,2,"2",("P42/ncm:2",),"-P 4ac 2ac","D4h^16"), 
(139,1,"",("I4/mmm",),"-I 4 2","D4h^17"), 
(140,1,"",("I4/mcm",),"-I 4 2c","D4h^18"), 
(141,1,"1",("I41/amd:1",),"I 4bw 2bw -1bw","D4h^19"), 
(141,2,"2",("I41/amd:2",),"-I 4bd 2","D4h^19"), 
(142,1,"1",("I41/acd:1",),"I 4bw 2aw -1bw","D4h^20"), 
(142,2,"2",("I41/acd:2",),"-I 4bd 2c","D4h^20"), 
(143,1,"",("P3",),"P 3","C3^1"), 
(144,1,"",("P31",),"P 31","C3^2"), 
(145,1,"",("P32",),"P 32","C3^3"), 
(146,1,"H",("R3:H",),"R 3","C3^4"), 
(146,2,"R",("R3:R",),"P 3*","C3^4"), 
(147,1,"",("P-3",),"-P 3","C3i^1"), 
(148,1,"H",("R-3:H",),"-R 3","C3i^2"), 
(148,2,"R",("R-3:R",),"-P 3*","C3i^2"), 
(149,1,"",("P312",),"P 3 2","D3^1"), 
(150,1,"",("P321",),"P 3 2\"","D3^2"), 
(151,1,"",("P3112",),"P 31 2c (0 0 1)","D3^3"), 
(152,1,"",("P3121",),"P 31 2\"","D3^4"), 
(153,1,"",("P3212",),"P 32 2c (0 0 -1)","D3^5"), 
(154,1,"",("P3221",),"P 32 2\"","D3^6"), 
(155,1,"H",("R32:H",),"R 3 2\"","D3^7"), 
(155,2,"R",("R32:R",),"P 3* 2","D3^7"), 
(156,1,"",("P3m1",),"P 3 -2\"","C3v^1"), 
(157,1,"",("P31m",),"P 3 -2","C3v^2"), 
(158,1,"",("P3c1",),"P 3 -2\"c","C3v^3"), 
(159,1,"",("P31c",),"P 3 -2c","C3v^4"), 
(160,1,"H",("R3m:H",),"R 3 -2\"","C3v^5"), 
(160,2,"R",("R3m:R",),"P 3* -2","C3v^5"), 
(161,1,"H",("R3c:H",),"R 3 -2\"c","C3v^6"), 
(161,2,"R",("R3c:R",),"P 3* -2n","C3v^6"), 
(162,1,"",("P-31m",),"-P 3 2","D3d^1"), 
(163,1,"",("P-31c",),"-P 3 2c","D3d^2"), 
(164,1,"",("P-3m1",),"-P 3 2\"","D3d^3"), 
(165,1,"",("P-3c1",),"-P 3 2\"c","D3d^4"), 
(166,1,"H",("R-3m:H",),"-R 3 2\"","D3d^5"), 
(166,2,"R",("R-3m:R",),"-P 3* 2","D3d^5"), 
(167,1,"H",("R-3c:H",),"-R 3 2\"c","D3d^6"), 
(167,2,"R",("R-3c:R",),"-P 3* 2n","D3d^6"), 
(168,1,"",("P6",),"P 6","C6^1"), 
(169,1,"",("P61",),"P 61","C6^2"), 
(170,1,"",("P65",),"P 65","C6^3"), 
(171,1,"",("P62",),"P 62","C6^4"), 
(172,1,"",("P64",),"P 64","C6^5"), 
(173,1,"",("P63",),"P 6c","C6^6"), 
(174,1,"",("P-6",),"P -6","C3h^1"), 
(175,1,"",("P6/m",),"-P 6","C6h^1"), 
(176,1,"",("P63/m",),"-P 6c","C6h^2"), 
(177,1,"",("P622",),"P 6 2","D6^1"), 
(178,1,"",("P6122",),"P 61 2 (0 0 -1)","D6^2"), 
(179,1,"",("P6522",),"P 65 2 (0 0 1)","D6^3"), 
(180,1,"",("P6222",),"P 62 2c (0 0 1)","D6^4"), 
(181,1,"",("P6422",),"P 64 2c (0 0 -1)","D6^5"), 
(182,1,"",("P6322",),"P 6c 2c","D6^6"), 
(183,1,"",("P6mm",),"P 6 -2","C6v^1"), 
(184,1,"",("P6cc",),"P 6 -2c","C6v^2"), 
(185,1,"",("P63cm",),"P 6c -2","C6v^3"), 
(186,1,"",("P63mc",),"P 6c -2c","C6v^4"), 
(187,1,"",("P-6m2",),"P -6 2","D3h^1"), 
(188,1,"",("P-6c2",),"P -6c 2","D3h^2"), 
(189,1,"",("P-62m",),"P -6 -2","D3h^3"), 
(190,1,"",("P-62c",),"P -6c -2c","D3h^4"), 
(191,1,"",("P6/mmm",),"-P 6 2","D6h^1"), 
(192,1,"",("P6/mcc",),"-P 6 2c","D6h^2"), 
(193,1,"",("P63/mcm",),"-P 6c 2","D6h^3"), 
(194,1,"",("P63/mmc",),"-P 6c 2c","D6h^4"), 
(195,1,"",("P23",),"P 2 2 3","T^1"), 
(196,1,"",("F23",),"F 2 2 3","T^2"), 
(197,1,"",("I23",),"I 2 2 3","T^3"), 
(198,1,"",("P213",),"P 2ac 2ab 3","T^4"), 
(199,1,"",("I213",),"I 2b 2c 3","T^5"), 
(200,1,"",("Pm-3",),"-P 2 2 3","Th^1"), 
(201,1,"1",("Pn-3:1",),"P 2 2 3 -1n","Th^2"), 
(201,2,"2",("Pn-3:2",),"-P 2ab 2bc 3","Th^2"), 
(202,1,"",("Fm-3",),"-F 2 2 3","Th^3"), 
(203,1,"1",("Fd-3:1",),"F 2 2 3 -1d","Th^4"), 
(203,2,"2",("Fd-3:2",),"-F 2uv 2vw 3","Th^4"), 
(204,1,"",("Im-3",),"-I 2 2 3","Th^5"), 
(205,1,"",("Pa-3",),"-P 2ac 2ab 3","Th^6"), 
(206,1,"",("Ia-3",),"-I 2b 2c 3","Th^7"), 
(207,1,"",("P432",),"P 4 2 3","O^1"), 
(208,1,"",("P4232",),"P 4n 2 3","O^2"), 
(209,1,"",("F432",),"F 4 2 3","O^3"), 
(210,1,"",("F4132",),"F 4d 2 3","O^4"), 
(211,1,"",("I432",),"I 4 2 3","O^5"), 
(212,1,"",("P4332",),"P 4acd 2ab 3","O^6"), 
(213,1,"",("P4132",),"P 4bd 2ab 3","O^7"), 
(214,1,"",("I4132",),"I 4bd 2c 3","O^8"), 
(215,1,"",("P-43m",),"P -4 2 3","Td^1"), 
(216,1,"",("F-43m",),"F -4 2 3","Td^2"), 
(217,1,"",("I-43m",),"I -4 2 3","Td^3"), 
(218,1,"",("P-43n",),"P -4n 2 3","Td^4"), 
(219,1,"",("F-43c",),"F -4c 2 3","Td^5"), 
(220,1,"",("I-43d",),"I -4bd 2c 3","Td^6"), 
(221,1,"",("Pm-3m",),"-P 4 2 3","Oh^1"), 
(222,1,"1",("Pn-3n:1",),"P 4 2 3 -1n","Oh^2"), 
(222,2,"2",("Pn-3n:2",),"-P 4a 2bc 3","Oh^2"), 
(223,1,"",("Pm-3n",),"-P 4n 2 3","Oh^3"), 
(224,1,"1",("Pn-3m:1",),"P 4n 2 3 -1n","Oh^4"), 
(224,2,"2",("Pn-3m:2",),"-P 4bc 2bc 3","Oh^4"), 
(225,1,"",("Fm-3m",),"-F 4 2 3","Oh^5"), 
(226,1,"",("Fm-3c",),"-F 4c 2 3","Oh^6"), 
(227,1,"1",("Fd-3m:1",),"F 4d 2 3 -1d","Oh^7"), 
(227,2,"2",("Fd-3m:2",),"-F 4vw 2vw 3","Oh^7"), 
(228,1,"1",("Fd-3c:1",),"F 4d 2 3 -1cd","Oh^8"), 
(228,2,"2",("Fd-3c:2",),"-F 4cvw 2vw 3","Oh^8"), 
(229,1,"",("Im-3m",),"-I 4 2 3","Oh^9"), 
(230,1,"",("Ia-3d",),"-I 4bd 2c 3","Oh^10"), 
]

parse_spacegroups={}
for i in range(len(spacegroups)):
    entry = spacegroups[i]
    parse_spacegroups[entry[4]]=i
    parse_spacegroups[entry[5]]=i
    for alt in entry[3]:
        parse_spacegroups[alt]=i
        parse_spacegroups[alt.upper()]=i
        parse_spacegroups[alt.lower()]=i
        if entry[1] == 1 and alt.find(':') != -1:
            falt = alt.split(':')[0]
            parse_spacegroups[falt]=i
            parse_spacegroups[falt.upper()]=i
            parse_spacegroups[falt.lower()]=i

    if entry[1] == 1:
        parse_spacegroups[entry[0]]=i
    parse_spacegroups[str(entry[0])+":"+str(entry[1])]=i
    parse_spacegroups[str(entry[0])+":"+entry[2]]=i

def find_index(parse):
    parse = str(parse).strip()
    try:
        return parse_spacegroups[parse]
    except KeyError:
        pass
    try:
        return parse_spacegroups[parse.replace(" ","").replace("_", " ")]
    except KeyError:
        pass
    raise Exception("Could not parse spacegroup:"+parse)

def spacegroup_get_schoenflies(parse):
    return spacegroups[find_index(parse)][5]

def spacegroup_get_hm(parse):
    return spacegroups[find_index(parse)][3][0]

def spacegroup_get_hall(parse):
    return spacegroups[find_index(parse)][4]

def spacegroup_get_number(parse):
    index = find_index(parse)
    return spacegroups[index][0]

def spacegroup_get_number_and_setting(parse):
    index = find_index(parse)
    return spacegroups[index][0],spacegroups[index][1]

def any_to_hall_symbol(spacegroup, setting=1):
    if is_sequence(spacegroup):
        parse = str(spacegroup[0])+":"+str(spacegroup[1])
    else:
        parse = str(spacegroup)
    return spacegroups[find_index(parse)][4]
 
 
lattice_translations = {
    "P":[],
    "I":["1n"],
    "R":["1r","1r"],
    "F":["1ab","1bc","1ac"],
    "A":["1bc"],
    "B":["1ac"],
    "C":["1ab"],
    "S":["1s","1s"],
    "T":["1t","1t"]
}
 
hall_rotations = {
 "1_"   : [[ 1, 0, 0],[ 0, 1, 0],[ 0, 0, 1]], #"+00 0+0 00+",
 "2x"   : [[ 1, 0, 0],[ 0,-1, 0],[ 0, 0,-1]], # "+00 0-0 00-",
 "2y"   : [[-1, 0, 0],[ 0, 1, 0],[ 0, 0,-1]], # "-00 0+0 00-",
 "2z"   : [[-1, 0, 0],[ 0,-1, 0],[ 0, 0, 1]], # "-00 0-0 00+",
 "2'"  : [[ 0,-1, 0],[-1, 0, 0],[ 0, 0,-1]], # "0-0 -00 00-", #z implied
 "2\""  : [[ 0, 1, 0],[ 1, 0, 0],[ 0, 0,-1]], # "0+0 +00 00-", #z implied
 "2x'" : [[-1, 0, 0],[ 0, 0,-1],[ 0,-1, 0]], # "-00 00- 0-0",
 "2x\"" : [[-1, 0, 0],[ 0, 0, 1],[ 0, 1, 0]], # "-00 00+ 0+0",
 "2y'" : [[ 0, 0,-1],[ 0,-1, 0],[-1, 0, 0]], # "00- 0-0 -00",
 "2y\"" : [[ 0, 0, 1],[ 0,-1, 0],[ 1, 0, 0]], # "00+ 0-0 +00",
 "2z'" : [[ 0,-1, 0],[-1, 0, 0],[ 0, 0,-1]], # "0-0 -00 00-",
 "2z\"" : [[ 0, 1, 0],[ 1, 0, 0],[ 0, 0,-1]], # "0+0 +00 00-",
 "3x"   : [[ 1, 0, 0],[ 0, 0,-1],[ 0, 1,-1]], # "+00 00- 0+-",
 "3y"   : [[-1, 0, 1],[ 0, 1, 0],[-1, 0, 0]], # "-0+ 0+0 -00",
 "3z"   : [[ 0,-1, 0],[ 1,-1, 0],[ 0, 0, 1]], # "0-0 +-0 00+",
 "3*"   : [[ 0, 0, 1],[ 1, 0, 0],[ 0, 1, 0]], # "00+ +00 0+0",
 "4x"   : [[ 1, 0, 0],[ 0, 0,-1],[ 0, 1, 0]], # "+00 00- 0+0",
 "4y"   : [[ 0, 0, 1],[ 0, 1, 0],[-1, 0, 0]], # "00+ 0+0 -00",
 "4z"   : [[ 0,-1, 0],[ 1, 0, 0],[ 0, 0, 1]], # "0-0 +00 00+",
 "6x"   : [[ 1, 0, 0],[ 0, 1,-1],[ 0, 1, 0]], # "+00 0+- 0+0",
 "6y"   : [[ 0, 0, 1],[ 0, 1, 0],[-1, 0, 1]], # "00+ 0+0 -0+",
 "6z"   : [[ 1,-1, 0],[ 1, 0, 0],[ 0, 0, 1]] # "+-0 +00 00+"                   
}

hall_translations = {
  'a': {6:[6, 0, 0]},
  'b': {0:[0, 6, 0]},
  'c': {0:[0, 0, 6]},
  'n': {6:[6, 6, 6]},
  'u': {3:[3, 0, 0]},
  'v': {0:[0, 3, 0]},
  'w': {0:[0, 0, 3]},
  'd': {3:[3, 3, 3]},
  '1': {2:[2, 6, -1],3:[3, 4, -1],4:[4, 3, -1],6:[6, 2, -1]},
  '2': {3:[3, 8, -1],6:[6, 4, -1]},
  '3': {4:[4, 9, -1]},
  '4': {6:[6, 8, -1]},
  '5': {6:[6, 10, -1]},
   ## extension to handle rhombohedral lattice as primitive
  'r': {4:[4, 8, 8]},
  's': {8:[8, 8, 4]},
  't': {8:[8, 4, 8]}                     
}

for key in hall_rotations:
    hall_rotations[key] = FracVector.create(hall_rotations[key])

def hall_rotation_term(code, prev_order, prev_axis_type, nbr_rotations, vector):
    code += "   "
    if code[0] == '-':
        improper = True
        code = code[1:]
    else:
        improper = False
    primitive_code = ""
    order = int(code[0])
    diagonal_reference_axis = '0'
    axis_type = '0'
    ptr = 2
    c = code[1]
    d = code[2]
    if c == 'x' or c == 'y' or c == 'z':
        if d == "'" or d=='"':
            diagonal_reference_axis = c
            c = code[2]
            ptr += 1
        axis_type = c
    elif c == "*":
        axis_type = c
    elif c == '"' or c == "'":
        if d == 'x' or d=='y' or d=='z':
            diagonal_reference_axis = d
            ptr += 1
        else:
            diagonal_reference_axis = prev_axis_type
    else:
        if order == 1:
            axis_type = '_'
        elif nbr_rotations == 0:
            axis_type = 'z'
        elif nbr_rotations == 2:
            axis_type = '*'
        elif prev_order == 2 or prev_order == 4:
            axis_type = 'x'
        else:
            axis_type = "'"
  
    code = code[0] + axis_type + code[1:]
    if axis_type == '_':
        primitive_code += "1"
    else:
        primitive_code += code[0:1]        

    if diagonal_reference_axis != '0':
        code = code[0] + diagonal_reference_axis + axis_type + code[ptr:];
        primitive_code += diagonal_reference_axis;
        ptr = 3;        
  
    lookup_code = code[0:ptr]
    rotation = hall_rotations[lookup_code]

    translation_string = ""    
    rotation_shift = 0
    vector_shift = FracVector.create([0,0,0])
    
    for i in range(len(code)):
        translation_code = code[i]
        if not translation_code in hall_translations:
            continue
        t = hall_translations[translation_code]
        if order in t:
            t = t[order]
        elif 0 in t:
            t = t[0]
        else:
            continue
        translation_string += translation_code 
        rotation_shift += t[1]
        vector_shift += FracVector.create(t)
    
    seitz = MutableFracVector.create([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
   
   
    if improper:
        primitive_code = '-' + primitive_code
        seitz[0:3,0:3] = [-x for x in rotation]
    else:
        seitz[0:3,0:3] = rotation
    
    seitz[0:3,3] = vector_shift

    if vector != None:
        m1 = MutableFracVector.create([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
        m2 = MutableFracVector.create([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
        m1[0:3,3] = vector
        m2[0:3,3] = -vector
        seitz = m1 * seitz * m2
        
    return seitz, order, axis_type, primitive_code
        
# Loosly inspired by algorithm from jmol source code, Miguel
def parse_hall_symbol(hall_symbol):
    elements = hall_symbol.split()
    
    if elements[0][0]=='-':
        centrosymmetric = True
        lattice_code = elements[0][1]
    else:
        centrosymmetric = False
        lattice_code = elements[0][0]
    
    lattice_extension = lattice_translations[lattice_code]
    if centrosymmetric:
        lattice_extension += ["-1"]

    if "(" in hall_symbol:
        if not ")" in hall_symbol:
            raise Exception("parse_hall_symbol: malformed hall symbol")
        hall_symbol_parts = hall_symbol.split("(")
        vector = hall_symbol_parts[1].split(")")[0].split()
        elements = hall_symbol_parts[0].split(" ")
    else:
        vector = None
    
    rotation_terms = []

    prev_order = 0
    prev_axis_type = "0"
    primitive_hall_symbol = "P"
    
    for i in range(1,len(elements)):
        element = elements[i]
        seitz, order, axis_type, primitive_code = hall_rotation_term(element, prev_order, prev_axis_type, i-1, vector)
        prev_order = order
        prev_axis_type = axis_type
        rotation_terms += [seitz]
        primitive_hall_symbol += " "+primitive_code

    if vector != None:
        primitive_hall_symbol += "("+" ".join(vector)+")"
    
    return primitive_hall_symbol, rotation_terms
    
def main():

    result = parse_hall_symbol('P 2y')
    print result
    
    pass

if __name__ == "__main__":
    main()   
    
    