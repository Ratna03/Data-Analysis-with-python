##### Process of loading nad reading data into python from various resources. #####

# import pandas library
import pandas as pd
# read the online file by the URL provides above, and assign it to variable "df"
path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(path,header=None)
df >>>>>>>>>>>>>>>>> Prints entire dataframe 

******* Output *******
	0	1	2	3	4	5	6	7	8	9	...	16	17	18	19	20	21	22	23	24	25
0	3	?	alfa-romero	gas	std	two	convertible	rwd	front	88.6	...	130	mpfi	3.47	2.68	9.00	111	5000	21	27	13495
1	3	?	alfa-romero	gas	std	two	convertible	rwd	front	88.6	...	130	mpfi	3.47	2.68	9.00	111	5000	21	27	16500
2	1	?	alfa-romero	gas	std	two	hatchback	rwd	front	94.5	...	152	mpfi	2.68	3.47	9.00	154	5000	19	26	16500
3	2	164	audi	gas	std	four	sedan	fwd	front	99.8	...	109	mpfi	3.19	3.40	10.00	102	5500	24	30	13950
4	2	164	audi	gas	std	four	sedan	4wd	front	99.4	...	136	mpfi	3.19	3.40	8.00	115	5500	18	22	17450
5	2	?	audi	gas	std	two	sedan	fwd	front	99.8	...	136	mpfi	3.19	3.40	8.50	110	5500	19	25	15250
6	1	158	audi	gas	std	four	sedan	fwd	front	105.8	...	136	mpfi	3.19	3.40	8.50	110	5500	19	25	17710
7	1	?	audi	gas	std	four	wagon	fwd	front	105.8	...	136	mpfi	3.19	3.40	8.50	110	5500	19	25	18920
8	1	158	audi	gas	turbo	four	sedan	fwd	front	105.8	...	131	mpfi	3.13	3.40	8.30	140	5500	17	20	23875
9	0	?	audi	gas	turbo	two	hatchback	4wd	front	99.5	...	131	mpfi	3.13	3.40	7.00	160	5500	16	22	?
10	2	192	bmw	gas	std	two	sedan	rwd	front	101.2	...	108	mpfi	3.50	2.80	8.80	101	5800	23	29	16430
11	0	192	bmw	gas	std	four	sedan	rwd	front	101.2	...	108	mpfi	3.50	2.80	8.80	101	5800	23	29	16925
12	0	188	bmw	gas	std	two	sedan	rwd	front	101.2	...	164	mpfi	3.31	3.19	9.00	121	4250	21	28	20970
13	0	188	bmw	gas	std	four	sedan	rwd	front	101.2	...	164	mpfi	3.31	3.19	9.00	121	4250	21	28	21105
14	1	?	bmw	gas	std	four	sedan	rwd	front	103.5	...	164	mpfi	3.31	3.19	9.00	121	4250	20	25	24565
15	0	?	bmw	gas	std	four	sedan	rwd	front	103.5	...	209	mpfi	3.62	3.39	8.00	182	5400	16	22	30760
16	0	?	bmw	gas	std	two	sedan	rwd	front	103.5	...	209	mpfi	3.62	3.39	8.00	182	5400	16	22	41315
17	0	?	bmw	gas	std	four	sedan	rwd	front	110.0	...	209	mpfi	3.62	3.39	8.00	182	5400	15	20	36880



df.head()  >>>>>> shows first 5 rows of data frame. 

******** Output *******
	0	1	2	3	4	5	6	7	8	9	...	16	17	18	19	20	21	22	23	24	25
0	3	?	alfa-romero	gas	std	two	convertible	rwd	front	88.6	...	130	mpfi	3.47	2.68	9.0	111	5000	21	27	13495
1	3	?	alfa-romero	gas	std	two	convertible	rwd	front	88.6	...	130	mpfi	3.47	2.68	9.0	111	5000	21	27	16500
2	1	?	alfa-romero	gas	std	two	hatchback	rwd	front	94.5	...	152	mpfi	2.68	3.47	9.0	154	5000	19	26	16500
3	2	164	audi	gas	std	four	sedan	fwd	front	99.8	...	109	mpfi	3.19	3.40	10.0	102	5500	24	30	13950
4	2	164	audi	gas	std	four	sedan	4wd	front	99.4	...	136	mpfi	3.19	3.40	8.0	115	5500	18	22	17450
5 rows × 26 columns


df.tail()  >>>>>>>>> shows last 5 rows of data frame.

******* Output *******

0	1	2	3	4	5	6	7	8	9	...	16	17	18	19	20	21	22	23	24	25
200	-1	95	volvo	gas	std	four	sedan	rwd	front	109.1	...	141	mpfi	3.78	3.15	9.5	114	5400	23	28	16845
201	-1	95	volvo	gas	turbo	four	sedan	rwd	front	109.1	...	141	mpfi	3.78	3.15	8.7	160	5300	19	25	19045
202	-1	95	volvo	gas	std	four	sedan	rwd	front	109.1	...	173	mpfi	3.58	2.87	8.8	134	5500	18	23	21485
203	-1	95	volvo	diesel	turbo	four	sedan	rwd	front	109.1	...	145	idi	3.01	3.40	23.0	106	4800	26	27	22470
204	-1	95	volvo	gas	turbo	four	sedan	rwd	front	109.1	...	141	mpfi	3.78	3.15	9.5	114	5400	19	25	22625
5 rows × 26 columns


df.dtypes  >>>>>>>>>>>>>>> check the data types

******* Output *******

0       int64
1      object
2      object
3      object
4      object
5      object
6      object
7      object
8      object
9     float64
10    float64
11    float64
12    float64
13      int64
14     object
15     object
16      int64
17     object
18     object
19     object
20    float64
21     object
22     object
23      int64
24      int64
25     object
dtype: object


df.describe() >>>>>>>>>>>>>>>>  Returns the statistical summary

******* Output *******

0	9	10	11	12	13	16	20	23	24
count	205.000000	205.000000	205.000000	205.000000	205.000000	205.000000	205.000000	205.000000	205.000000	205.000000
mean	0.834146	98.756585	174.049268	65.907805	53.724878	2555.565854	126.907317	10.142537	25.219512	30.751220
std	1.245307	6.021776	12.337289	2.145204	2.443522	520.680204	41.642693	3.972040	6.542142	6.886443
min	-2.000000	86.600000	141.100000	60.300000	47.800000	1488.000000	61.000000	7.000000	13.000000	16.000000
25%	0.000000	94.500000	166.300000	64.100000	52.000000	2145.000000	97.000000	8.600000	19.000000	25.000000
50%	1.000000	97.000000	173.200000	65.500000	54.100000	2414.000000	120.000000	9.000000	24.000000	30.000000
75%	2.000000	102.400000	183.100000	66.900000	55.500000	2935.000000	141.000000	9.400000	30.000000	34.000000
max	3.000000	120.900000	208.100000	72.300000	59.800000	4066.000000	326.000000	23.000000	49.000000	54.000000


df.describe(include = "all") >>>>>>>> Returns the whole statistical summary including null values.

******* Output *******


0	1	2	3	4	5	6	7	8	9	...	16	17	18	19	20	21	22	23	24	25
count	205.000000	205	205	205	205	205	205	205	205	205.000000	...	205.000000	205	205	205	205.000000	205	205	205.000000	205.000000	205
unique	NaN	52	22	2	2	3	5	3	2	NaN	...	NaN	8	39	37	NaN	60	24	NaN	NaN	187
top	NaN	?	toyota	gas	std	four	sedan	fwd	front	NaN	...	NaN	mpfi	3.62	3.40	NaN	68	5500	NaN	NaN	?
freq	NaN	41	32	185	168	114	96	120	202	NaN	...	NaN	94	23	20	NaN	19	37	NaN	NaN	4
mean	0.834146	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	98.756585	...	126.907317	NaN	NaN	NaN	10.142537	NaN	NaN	25.219512	30.751220	NaN
std	1.245307	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	6.021776	...	41.642693	NaN	NaN	NaN	3.972040	NaN	NaN	6.542142	6.886443	NaN
min	-2.000000	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	86.600000	...	61.000000	NaN	NaN	NaN	7.000000	NaN	NaN	13.000000	16.000000	NaN
25%	0.000000	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	94.500000	...	97.000000	NaN	NaN	NaN	8.600000	NaN	NaN	19.000000	25.000000	NaN
50%	1.000000	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	97.000000	...	120.000000	NaN	NaN	NaN	9.000000	NaN	NaN	24.000000	30.000000	NaN
75%	2.000000	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	102.400000	...	141.000000	NaN	NaN	NaN	9.400000	NaN	NaN	30.000000	34.000000	NaN
max	3.000000	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	120.900000	...	326.000000	NaN	NaN	NaN	23.000000	NaN	NaN	49.000000	54.000000	NaN
11 rows × 26 columns


df.info >>>>>>>>>>>>>>> Provides concise summary of dataset

******* Output *******

<bound method DataFrame.info of      0    1            2       3      4     5            6    7      8   \
0     3    ?  alfa-romero     gas    std   two  convertible  rwd  front   
1     3    ?  alfa-romero     gas    std   two  convertible  rwd  front   
2     1    ?  alfa-romero     gas    std   two    hatchback  rwd  front   
3     2  164         audi     gas    std  four        sedan  fwd  front   
4     2  164         audi     gas    std  four        sedan  4wd  front   
5     2    ?         audi     gas    std   two        sedan  fwd  front   
6     1  158         audi     gas    std  four        sedan  fwd  front   
7     1    ?         audi     gas    std  four        wagon  fwd  front   
8     1  158         audi     gas  turbo  four        sedan  fwd  front   
9     0    ?         audi     gas  turbo   two    hatchback  4wd  front   
10    2  192          bmw     gas    std   two        sedan  rwd  front   
11    0  192          bmw     gas    std  four        sedan  rwd  front   
12    0  188          bmw     gas    std   two        sedan  rwd  front   
13    0  188          bmw     gas    std  four        sedan  rwd  front   
14    1    ?          bmw     gas    std  four        sedan  rwd  front   
15    0    ?          bmw     gas    std  four        sedan  rwd  front   
16    0    ?          bmw     gas    std   two        sedan  rwd  front   
17    0    ?          bmw     gas    std  four        sedan  rwd  front   
18    2  121    chevrolet     gas    std   two    hatchback  fwd  front   
19    1   98    chevrolet     gas    std   two    hatchback  fwd  front   
20    0   81    chevrolet     gas    std  four        sedan  fwd  front   
21    1  118        dodge     gas    std   two    hatchback  fwd  front   
22    1  118        dodge     gas    std   two    hatchback  fwd  front   
23    1  118        dodge     gas  turbo   two    hatchback  fwd  front   
24    1  148        dodge     gas    std  four    hatchback  fwd  front   
25    1  148        dodge     gas    std  four        sedan  fwd  front   
26    1  148        dodge     gas    std  four        sedan  fwd  front   
27    1  148        dodge     gas  turbo     ?        sedan  fwd  front   
28   -1  110        dodge     gas    std  four        wagon  fwd  front   
29    3  145        dodge     gas  turbo   two    hatchback  fwd  front   
..   ..  ...          ...     ...    ...   ...          ...  ...    ...   
175  -1   65       toyota     gas    std  four    hatchback  fwd  front   
176  -1   65       toyota     gas    std  four        sedan  fwd  front   
177  -1   65       toyota     gas    std  four    hatchback  fwd  front   
178   3  197       toyota     gas    std   two    hatchback  rwd  front   
179   3  197       toyota     gas    std   two    hatchback  rwd  front   
180  -1   90       toyota     gas    std  four        sedan  rwd  front   
181  -1    ?       toyota     gas    std  four        wagon  rwd  front   
182   2  122   volkswagen  diesel    std   two        sedan  fwd  front   
183   2  122   volkswagen     gas    std   two        sedan  fwd  front   
184   2   94   volkswagen  diesel    std  four        sedan  fwd  front   
185   2   94   volkswagen     gas    std  four        sedan  fwd  front   
186   2   94   volkswagen     gas    std  four        sedan  fwd  front   
187   2   94   volkswagen  diesel  turbo  four        sedan  fwd  front   
188   2   94   volkswagen     gas    std  four        sedan  fwd  front   
189   3    ?   volkswagen     gas    std   two  convertible  fwd  front   
190   3  256   volkswagen     gas    std   two    hatchback  fwd  front   
191   0    ?   volkswagen     gas    std  four        sedan  fwd  front   
192   0    ?   volkswagen  diesel  turbo  four        sedan  fwd  front   
193   0    ?   volkswagen     gas    std  four        wagon  fwd  front   
194  -2  103        volvo     gas    std  four        sedan  rwd  front   
195  -1   74        volvo     gas    std  four        wagon  rwd  front   
196  -2  103        volvo     gas    std  four        sedan  rwd  front   
197  -1   74        volvo     gas    std  four        wagon  rwd  front   
198  -2  103        volvo     gas  turbo  four        sedan  rwd  front   
199  -1   74        volvo     gas  turbo  four        wagon  rwd  front   
200  -1   95        volvo     gas    std  four        sedan  rwd  front   
201  -1   95        volvo     gas  turbo  four        sedan  rwd  front   
202  -1   95        volvo     gas    std  four        sedan  rwd  front   
203  -1   95        volvo  diesel  turbo  four        sedan  rwd  front   
204  -1   95        volvo     gas  turbo  four        sedan  rwd  front   

        9   ...     16    17    18    19     20   21    22  23  24     25  
0     88.6  ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  13495  
1     88.6  ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  16500  
2     94.5  ...    152  mpfi  2.68  3.47   9.00  154  5000  19  26  16500  
3     99.8  ...    109  mpfi  3.19  3.40  10.00  102  5500  24  30  13950  
4     99.4  ...    136  mpfi  3.19  3.40   8.00  115  5500  18  22  17450  
5     99.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  15250  
6    105.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  17710  
7    105.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  18920  
8    105.8  ...    131  mpfi  3.13  3.40   8.30  140  5500  17  20  23875  
9     99.5  ...    131  mpfi  3.13  3.40   7.00  160  5500  16  22      ?  
10   101.2  ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16430  
11   101.2  ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16925  
12   101.2  ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  20970  
13   101.2  ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  21105  
14   103.5  ...    164  mpfi  3.31  3.19   9.00  121  4250  20  25  24565  
15   103.5  ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  30760  
16   103.5  ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  41315  
17   110.0  ...    209  mpfi  3.62  3.39   8.00  182  5400  15  20  36880  
18    88.4  ...     61  2bbl  2.91  3.03   9.50   48  5100  47  53   5151  
19    94.5  ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6295  
20    94.5  ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6575  
21    93.7  ...     90  2bbl  2.97  3.23   9.41   68  5500  37  41   5572  
22    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6377  
23    93.7  ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   7957  
24    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6229  
25    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6692  
26    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   7609  
27    93.7  ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   8558  
28   103.3  ...    122  2bbl  3.34  3.46   8.50   88  5000  24  30   8921  
29    95.9  ...    156   mfi  3.60  3.90   7.00  145  5000  19  24  12964  
..     ...  ...    ...   ...   ...   ...    ...  ...   ...  ..  ..    ...  
175  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32   9988  
176  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  10898  
177  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  11248  
178  102.9  ...    171  mpfi  3.27  3.35   9.30  161  5200  20  24  16558  
179  102.9  ...    171  mpfi  3.27  3.35   9.30  161  5200  19  24  15998  
180  104.5  ...    171  mpfi  3.27  3.35   9.20  156  5200  20  24  15690  
181  104.5  ...    161  mpfi  3.27  3.35   9.20  156  5200  19  24  15750  
182   97.3  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7775  
183   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   7975  
184   97.3  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7995  
185   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8195  
186   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8495  
187   97.3  ...     97   idi  3.01  3.40  23.00   68  4500  37  42   9495  
188   97.3  ...    109  mpfi  3.19  3.40  10.00  100  5500  26  32   9995  
189   94.5  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29  11595  
190   94.5  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29   9980  
191  100.4  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  24  13295  
192  100.4  ...     97   idi  3.01  3.40  23.00   68  4500  33  38  13845  
193  100.4  ...    109  mpfi  3.19  3.40   9.00   88  5500  25  31  12290  
194  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  12940  
195  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  13415  
196  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  15985  
197  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  16515  
198  104.3  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18420  
199  104.3  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18950  
200  109.1  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  16845  
201  109.1  ...    141  mpfi  3.78  3.15   8.70  160  5300  19  25  19045  
202  109.1  ...    173  mpfi  3.58  2.87   8.80  134  5500  18  23  21485  
203  109.1  ...    145   idi  3.01  3.40  23.00  106  4800  26  27  22470  
204  109.1  ...    141  mpfi  3.78  3.15   9.50  114  5400  19  25  22625  

[205 rows x 26 columns]>





