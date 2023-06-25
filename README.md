# VBCr-Automation
Tested on Windows 10<br>
Automatically increment keyspace 66 using VBCr VanitySearch prefix finder SO YOU DON'T HAVE TO<br>
first download VBCr.exe from https://github.com/WanderingPhilosopher/VanBitCrackenRandom2  <br>
python3 66.py runs entire keyspace then loops to beginning. 
creates continue .pkl file to continue from last checkpoint in case of interuption or ctlr+c (default 60 seconds) <br>
Afrer interruption just run python3 66.py to continue from last checkpoint<br>
python3 runvbc_loop.py completes keyspace than starts over indefinitely until killed no checkpoint<br>
python3 runvbc-cpu.py cpu only adjust number of cpu's  default is 3 -t 3 in code<br>
automatically creates found folder for found in each increment i.e 200.txt 201.txt  till end of keyspace 3ff.txt (keeps found in order)<br>
adjust time for each increment default is 500 seconds<br>
adust the prefix length to search for  default is 13zb1hQ for keyspace 66<br>
if using cpu's also set the number -t (number)



Example<br>

 [00:00:07:11 Run Time][Total 47.01 MK/s][GPU 43.38 MK/s][Keys 20,226,323,456][Found 20][Rekeys: 3]<br>
Random Key :  20E334D8A65620F84<br>
Random Key :  20EEFE5210850F40E<br>
Random Key :  20E545B4508FCFB13<br>
Random Key :  20EA491A1B6893ABC<br>
Random Key :  20E8D31F225431608<br>
Random Key :  20EF67E4032B9341F<br>
Random Key :  20EE35DFF595E0BE0<br>
 [00:00:07:17 Run Time][Total 46.40 MK/s][GPU 42.66 MK/s][Keys 20,508,148,736][Found 20][Rekeys: 4]<br>
<br>
PubAddress: 13zb1HQJiHKfPjUhmWLe4GPnr3m7mjhMCd<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVaB3VZbP7wecKNT851<br>
Priv (HEX): 20EED274E29C710AE (66 bit)<br>
 [00:00:07:21 Run Time][Total 46.03 MK/s][GPU 42.29 MK/s][Keys 20,695,656,448][Found 21][Rekeys: 4]<br>
<br>
PubAddress: 13Zb1HqCXrZhkDCHDfo3GMgN3Du1BTDRjx<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVXHohRfJLrMy5fjqaK<br>
Priv (HEX): 20E545B4509CA0F0F (66 bit)<br>
 [00:00:07:31 Run Time][Total 45.67 MK/s][GPU 42.01 MK/s][Keys 21,171,546,112][Found 22][Rekeys: 4]<br>

PubAddress: 13ZB1HqWoZmFaKiEVJkeTDzDoHeU7AAKXW<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVXHohRfsrTy9LsNgAU<br>
Priv (HEX): 20E545B450A9267D0 (66 bit)<br>
 [00:00:07:46 Run Time][Total 47.09 MK/s][GPU 43.30 MK/s][Keys 21,859,034,112][Found 23][Rekeys: 4]<br>

PubAddress: 13ZB1HqPPLdfTu9R83VYJEMQqAwWE9mpCX<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVZP57deNEnojW6eUH2<br>
Priv (HEX): 20EC326B16300641E (66 bit)<br>
 [00:00:08:11 Run Time][Total 47.83 MK/s][GPU 43.94 MK/s][Keys 23,042,325,504][Found 24][Rekeys: 4]<br>

PubAddress: 13Zb1HQXzppCgxfYBHwVXvcpwaCZXSUGgd<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVWRc8EAzXbdanmrFBc<br>
Priv (HEX): 20E267DDEE2FEDF9B (66 bit)<br>
 [00:00:08:17 Run Time][Total 47.19 MK/s][GPU 43.39 MK/s][Keys 23,336,275,968][Found 25][Rekeys: 4]  ^CVBCr v2.00<br>
 Search For: 13zb1hQ [Compressed, Case unsensitive] (Lookup size 4)<br>
 Started on: Fri Jun 16 16:55:07 2023<br>
 Randomness: New Random Keys Every 5000 Mkeys<br>
  Beg Range: 20F00000000000001 (66 bit)<br>
  End Range: 21000000000000000 (66 bit)<br>
  Rng Width: FFFFFFFFFFFFFF (56 bit)<br>
CPU Threads: 3<br>
<br>
Random Key :  20FEFE9737CDBEC80<br>
Random Key :  20FB7C17F33783AB4<br>
Random Key :  20FC16F3D1B1AE762GPU: GPU #0 NVIDIA GeForce GT 1030 (3x128 cores) Grid(24x128)<br>
<br>
Random Key :  20F93F02252D2E9F4<br>
Random Key :  20F681A928E7755AF<br>
Random Key :  20F6F991BFB67A061<br>
Random Key :  20FD0DD9C448B7B39<br>
Random Key :  20FB5DD320ABBF893<br>
Random Key :  20FA8E341C7885F2A<br>
Random Key :  20F313BBC9AAA36E9<br>
Random Key :  20F147B4D0F2AE255<br>
Random Key :  20F6617ECDF77DA78<br>
 [00:00:00:31 Run Time][Total 47.22 MK/s][GPU 43.38 MK/s][Keys 1,454,391,296][Found 0][Rekeys: 0]<br>
<br>
PubAddress: 13zB1hqAmqthrWvsjGGk6hQ2rbLcV3NxHn<br>
Priv (WIF): p2pkh: KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qZVebbJ63fmEeLh5nUAK<br>
Priv (HEX): 20FD78C93F78C192C (66 bit)<br>
 [00:00:00:33 Run Time][Total 47.10 MK/s][GPU 43.19 MK/s][Keys 1,547,363,328][Found 1][Rekeys: 0]<br>

<B>If this program  helps find your hidden treasures :  donations<br>
 Bitcoin    bc1qus09g0n5jwg79gje76zxqmzt3gpw80dcqspsmm <br>
 Litecoin   ltc1q5qtw6fhuqcarv8ysfv7c52gyyfnys3gzlds5s8</b>
