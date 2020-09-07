
# print "Top"
# a = raw_input("Enter info: ") # input test
# print a
# list1 = [1, 2, 3, 4, 5] # list test
# for num in range(0, len(list1)):
#     print list1[num]
# THIS TAKES .TSV FILES
team_string = "200	76ers GC	16	1920	384	1058	421	726	0.58	165	341	0.484	125	166	289	152	149	33	935	123	387	699	0.554	105	250	0.42	126	170	235	124	177	33\n\
201	Bucks Gaming	16	1950	390	1022	406	713	0.569	152	300	0.507	104	183	234	127	170	31	949	73	390	684	0.57	109	256	0.426	96	189	244	129	172	34\n\
202	Wizards District Gaming	16	1920	384	1012	410	706	0.581	119	266	0.447	118	197	252	131	184	39	982	30	400	718	0.557	123	276	0.446	111	162	248	150	171	30\n\
204	Cavs Legion GC	16	1935	387	960	393	680	0.578	100	223	0.448	77	158	261	160	159	34	1030	-70	410	690	0.594	150	282	0.532	113	198	286	131	200	29\n\
205	Celtics Crossover Gaming	16	1935	387	1071	419	717	0.584	164	327	0.502	107	171	277	172	164	39	964	107	388	688	0.564	129	304	0.424	116	179	255	134	205	35\n\
208	Grizz Gaming	16	1920	384	997	406	715	0.568	120	273	0.44	118	193	250	132	149	31	899	98	362	663	0.546	131	270	0.485	84	184	234	109	178	27\n\
209	Hawks Talon GC	16	1920	384	960	390	733	0.532	116	259	0.448	130	169	223	123	181	36	1082	-122	437	710	0.615	135	273	0.495	91	203	291	142	161	48\n\
210	Heat Check Gaming	16	1920	384	1016	415	749	0.554	126	269	0.468	117	203	269	165	221	34	1102	-86	434	766	0.567	158	321	0.492	127	204	288	172	203	46\n\
212	Jazz Gaming	16	1935	387	995	414	700	0.591	118	262	0.45	101	191	295	128	170	42	1014	-19	413	688	0.6	123	255	0.482	76	172	251	141	145	33\n\
213	Kings Guard Gaming	16	1920	384	968	372	657	0.566	164	320	0.513	91	192	242	119	168	38	937	31	384	680	0.565	117	266	0.44	90	181	267	133	155	32\n\
214	Knicks Gaming	16	1920	384	964	389	710	0.548	128	301	0.425	121	195	264	135	235	32	1079	-115	445	770	0.578	146	313	0.466	111	192	295	195	178	38\n\
215	Lakers Gaming	16	1950	390	845	334	669	0.499	109	289	0.377	104	175	216	132	194	49	989	-144	398	704	0.565	119	251	0.474	108	203	245	152	162	37\n\
216	Magic Gaming	16	1920	384	945	385	664	0.58	119	281	0.423	94	174	246	123	145	33	889	56	362	650	0.557	113	237	0.477	99	170	213	113	156	30\n\
217	Mavs Gaming	16	1920	384	1004	417	688	0.606	127	246	0.516	99	197	262	133	181	44	956	48	386	729	0.529	121	286	0.423	140	157	240	147	156	29\n\
218	NetsGC	16	1935	387	961	389	673	0.578	110	256	0.43	92	192	254	135	178	36	1047	-86	421	740	0.569	138	298	0.463	115	184	264	151	159	33\n\
220	Pacers Gaming	16	1920	384	996	408	700	0.583	127	256	0.496	99	164	255	119	129	28	943	53	379	688	0.551	130	286	0.455	128	182	238	98	162	43\n\
221	Pistons GT	16	1920	384	967	399	714	0.559	109	256	0.426	116	158	284	125	204	26	1148	-181	466	735	0.634	155	283	0.548	99	189	316	153	161	44\n\
222	Raptors Uprising GC	16	1920	384	919	372	682	0.545	132	273	0.484	94	178	254	149	178	31	979	-60	398	693	0.574	126	260	0.485	107	203	248	148	187	31\n\
227	T-Wolves Gaming	16	1920	384	1024	421	693	0.608	122	241	0.506	94	197	291	145	166	38	931	93	367	686	0.535	127	282	0.45	115	166	233	126	186	25\n\
228	Blazer5 Gaming	16	1950	390	1062	429	729	0.588	135	277	0.487	117	192	265	165	164	33	889	173	354	665	0.532	124	288	0.431	100	168	271	127	213	46\n\
229	Warriors Gaming Squad	16	1920	384	941	382	691	0.553	128	257	0.498	123	179	231	144	178	32	943	-2	390	663	0.588	111	236	0.47	89	168	252	139	180	36"

team_list = team_string.split("\n")
# print team_list
# print len(team_list)
for i in range(0, 21):
    team_list[i] = team_list[i].split("\t")     # CHANGE THIS TO ", " IF .CSV!
# print team_list
query = "Kings Guard Gaming"        # THIS DEPENDS ON USER OPTION
print "Stats for", query, "(out of #1-#21)"
# print len(team_list[0])
# compare kings to other teams
# take out specific category, and kings' value for that category
# or take out which total pts more than opponents totals
query_index = -1
for index in range(0, len(team_list)):
    if (team_list[index][1]) == query:
        query_index = index
# print query_pts
# get all pts, sort them, find out which one is
# query_pts = team_list[query_index][5]
# points_list = []
# for index in range(0, len(team_list)):
#     points_list.append(team_list[index][5])
# points_list.sort(reverse = True, key = int)
# print points_list
# query_pts_rank = points_list.index(query_pts)+1
# print query_pts_rank      # POINT RANK IS WORKING
#
# get all FG%, sort them, find out which one is
###     OFFENSE
query_fgp = team_list[query_index][8]
fgp_list = []
for index in range(0, len(team_list)):
    fgp_list.append(team_list[index][8])
fgp_list.sort(reverse = True, key = float)
# print fgp_list
query_fgp_rank = fgp_list.index(query_fgp)+1
print "Ranking for Field Goal Percentage: #",
# print fgp_list[query_index]
print query_fgp_rank        # WORKING

query_fg3 = team_list[query_index][11]
fg3_list = []
for index in range(0, len(team_list)):
    fg3_list.append(team_list[index][11])
fg3_list.sort(reverse = True, key = float)
# print fg3_list
query_fg3_rank = fg3_list.index(query_fg3)+1
print "Ranking for Three-Pointer Percentage: #",
# print fgp_list[query_index]
print query_fg3_rank        # WORKING

###     DEFENSE

query_steal = team_list[query_index][15]
steal_list = []
for index in range(0, len(team_list)):
    steal_list.append(team_list[index][15])
steal_list.sort(reverse = True, key = int)
# print steal_list
query_steal_rank = steal_list.index(query_steal)+1
print "Ranking for Total Steals: #",
# print query_fgp
# print fgp_list[query_index]
print query_steal_rank      # WORKING

query_block = team_list[query_index][17]
block_list = []
for index in range(0, len(team_list)):
    block_list.append(team_list[index][17])
block_list.sort(reverse = True, key = float)
# print block_list
query_block_rank = block_list.index(query_block)+1
print "Ranking for Total Blocks: #",
# print fgp_list[query_index]
print query_block_rank      # WORKING (but chooses lower one)

query_TO = team_list[query_index][16]
TO_list = []
for index in range(0, len(team_list)):
    TO_list.append(team_list[index][16])
TO_list.sort(key = int)
# print TO_list
query_TO_rank = TO_list.index(query_TO)+1
print "Ranking for Least Turnovers: #",
# print fgp_list[query_index]
print query_TO_rank

#       SUPPORT

query_reb = team_list[query_index][12]
reb_list = []
for index in range(0, len(team_list)):
    reb_list.append(team_list[index][12])
reb_list.sort(reverse = True, key = int)
# print reb_list
query_reb_rank = reb_list.index(query_reb)+1
# print query_reb
print "Ranking for Total Rebounds: #",
# print fgp_list[query_index]
print query_reb_rank

query_ast = team_list[query_index][14]
ast_list = []
for index in range(0, len(team_list)):
    ast_list.append(team_list[index][14])
ast_list.sort(reverse=True, key=int)
# print ast_list
query_ast_rank = ast_list.index(query_ast)+1
# print query_ast
print "Ranking for Total Assists: #",
# print fgp_list[query_index]
print query_ast_rank
