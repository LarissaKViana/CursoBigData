{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2.3\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "'numVotesg'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\pandas\\core\\indexes\\base.py:3805\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3803'>3804</a>\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m-> <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3804'>3805</a>\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_engine\u001b[39m.\u001b[39;49mget_loc(casted_key)\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3805'>3806</a>\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mKeyError\u001b[39;00m \u001b[39mas\u001b[39;00m err:\n",
      "File \u001b[1;32mindex.pyx:167\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mindex.pyx:196\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mpandas\\\\_libs\\\\hashtable_class_helper.pxi:7081\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mpandas\\\\_libs\\\\hashtable_class_helper.pxi:7089\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'numVotesg'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\unidade.copacabana\\Documents\\BigDataSenac\\aula11_21102024.py\u001b[0m in \u001b[0;36mline 3\n\u001b[0;32m      <a href='file:///c%3A/Users/unidade.copacabana/Documents/BigDataSenac/aula11_21102024.py?line=25'>26</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mpandas\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mpd\u001b[39;00m\n\u001b[0;32m      <a href='file:///c%3A/Users/unidade.copacabana/Documents/BigDataSenac/aula11_21102024.py?line=26'>27</a>\u001b[0m \u001b[39mprint\u001b[39m(pd\u001b[39m.\u001b[39m__version__)\n\u001b[1;32m----> <a href='file:///c%3A/Users/unidade.copacabana/Documents/BigDataSenac/aula11_21102024.py?line=27'>28</a>\u001b[0m df_filme_serie[\u001b[39m'\u001b[39m\u001b[39maverageRating_and_numVotes\u001b[39m\u001b[39m'\u001b[39m]\u001b[39m=\u001b[39m\u001b[39mstr\u001b[39m(df_filme_serie[\u001b[39m'\u001b[39m\u001b[39maverageRating\u001b[39m\u001b[39m'\u001b[39m])\u001b[39m+\u001b[39m\u001b[39m'\u001b[39m\u001b[39m-\u001b[39m\u001b[39m'\u001b[39m\u001b[39m+\u001b[39m\u001b[39mstr\u001b[39m(df_filme_serie[\u001b[39m'\u001b[39;49m\u001b[39mnumVotesg\u001b[39;49m\u001b[39m'\u001b[39;49m])\n\u001b[0;32m      <a href='file:///c%3A/Users/unidade.copacabana/Documents/BigDataSenac/aula11_21102024.py?line=28'>29</a>\u001b[0m \u001b[39mprint\u001b[39m(df_filme_serie\u001b[39m.\u001b[39mhead())  \u001b[39m# Exibe as primeiras linhas\u001b[39;00m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\pandas\\core\\frame.py:4102\u001b[0m, in \u001b[0;36mDataFrame.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/frame.py?line=4099'>4100</a>\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mcolumns\u001b[39m.\u001b[39mnlevels \u001b[39m>\u001b[39m \u001b[39m1\u001b[39m:\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/frame.py?line=4100'>4101</a>\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_getitem_multilevel(key)\n\u001b[1;32m-> <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/frame.py?line=4101'>4102</a>\u001b[0m indexer \u001b[39m=\u001b[39m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mcolumns\u001b[39m.\u001b[39;49mget_loc(key)\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/frame.py?line=4102'>4103</a>\u001b[0m \u001b[39mif\u001b[39;00m is_integer(indexer):\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/frame.py?line=4103'>4104</a>\u001b[0m     indexer \u001b[39m=\u001b[39m [indexer]\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\pandas\\core\\indexes\\base.py:3812\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3806'>3807</a>\u001b[0m     \u001b[39mif\u001b[39;00m \u001b[39misinstance\u001b[39m(casted_key, \u001b[39mslice\u001b[39m) \u001b[39mor\u001b[39;00m (\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3807'>3808</a>\u001b[0m         \u001b[39misinstance\u001b[39m(casted_key, abc\u001b[39m.\u001b[39mIterable)\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3808'>3809</a>\u001b[0m         \u001b[39mand\u001b[39;00m \u001b[39many\u001b[39m(\u001b[39misinstance\u001b[39m(x, \u001b[39mslice\u001b[39m) \u001b[39mfor\u001b[39;00m x \u001b[39min\u001b[39;00m casted_key)\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3809'>3810</a>\u001b[0m     ):\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3810'>3811</a>\u001b[0m         \u001b[39mraise\u001b[39;00m InvalidIndexError(key)\n\u001b[1;32m-> <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3811'>3812</a>\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mKeyError\u001b[39;00m(key) \u001b[39mfrom\u001b[39;00m \u001b[39merr\u001b[39;00m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3812'>3813</a>\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mTypeError\u001b[39;00m:\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3813'>3814</a>\u001b[0m     \u001b[39m# If we have a listlike key, _check_indexing_error will raise\u001b[39;00m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3814'>3815</a>\u001b[0m     \u001b[39m#  InvalidIndexError. Otherwise we fall through and re-raise\u001b[39;00m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3815'>3816</a>\u001b[0m     \u001b[39m#  the TypeError.\u001b[39;00m\n\u001b[0;32m   <a href='file:///c%3A/Users/unidade.copacabana/AppData/Roaming/Python/Python311/site-packages/pandas/core/indexes/base.py?line=3816'>3817</a>\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_check_indexing_error(key)\n",
      "\u001b[1;31mKeyError\u001b[0m: 'numVotesg'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "print(pd.__version__)\n",
    "df_filme_serie['averageRating_and_numVotes']=str(df_filme_serie['averageRating'])+'-'+str(df_filme_serie['numVotesg'])\n",
    "print(df_filme_serie.head())  # Exibe as primeiras linhas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2.3\n",
      "          id             title          type                  genres  \\\n",
      "0  tt0903747      Breaking Bad      tvSeries  Crime, Drama, Thriller   \n",
      "1  tt5491994   Planet Earth II  tvMiniSeries             Documentary   \n",
      "2  tt0185906  Band of Brothers  tvMiniSeries     Drama, History, War   \n",
      "3  tt0795176      Planet Earth  tvMiniSeries     Documentary, Family   \n",
      "4  tt5152226      Tree of Life      tvSeries                   Drama   \n",
      "\n",
      "   averageRating  numVotes  releaseYear  \n",
      "0            9.5   2220756         2008  \n",
      "1            9.5    161283         2016  \n",
      "2            9.4    542837         2001  \n",
      "3            9.4    222817         2006  \n",
      "4            9.4     11445         2014  \n",
      "             id                 title      type                    genres  \\\n",
      "6030  tt3089778         The Treatment     movie  Crime, Mystery, Thriller   \n",
      "6031  tt0252684                 Manic     movie                     Drama   \n",
      "6032  tt0072353          Going Places     movie     Action, Comedy, Crime   \n",
      "6033  tt7695916       Tell Me a Story  tvSeries           Drama, Thriller   \n",
      "6034  tt0063829  Yours, Mine and Ours     movie            Comedy, Family   \n",
      "\n",
      "      averageRating  numVotes  releaseYear  \n",
      "6030            7.1     10190         2014  \n",
      "6031            7.1     10171         2001  \n",
      "6032            7.1     10125         1974  \n",
      "6033            7.1     10084         2018  \n",
      "6034            7.1     10056         1968  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "print(pd.__version__)\n",
    "#ACESSO À DATASETS EXTERNOS:\n",
    "##https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data\n",
    "\n",
    "df_filme_serie = pd.read_csv('FilmesSeries.csv')\n",
    "print(df_filme_serie.head())  # Exibe as primeiras linhas\n",
    "print(df_filme_serie.tail())  # Exibe as cinco últimas linhas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2.3\n",
      "          id             title          type                  genres  \\\n",
      "0  tt0903747      Breaking Bad      tvSeries  Crime, Drama, Thriller   \n",
      "1  tt5491994   Planet Earth II  tvMiniSeries             Documentary   \n",
      "2  tt0185906  Band of Brothers  tvMiniSeries     Drama, History, War   \n",
      "3  tt0795176      Planet Earth  tvMiniSeries     Documentary, Family   \n",
      "4  tt5152226      Tree of Life      tvSeries                   Drama   \n",
      "\n",
      "   averageRating  numVotes  releaseYear  \\\n",
      "0            9.5   2220756         2008   \n",
      "1            9.5    161283         2016   \n",
      "2            9.4    542837         2001   \n",
      "3            9.4    222817         2006   \n",
      "4            9.4     11445         2014   \n",
      "\n",
      "                          averageRating_and_numVotes  \n",
      "0  0       9.5\\n1       9.5\\n2       9.4\\n3      ...  \n",
      "1  0       9.5\\n1       9.5\\n2       9.4\\n3      ...  \n",
      "2  0       9.5\\n1       9.5\\n2       9.4\\n3      ...  \n",
      "3  0       9.5\\n1       9.5\\n2       9.4\\n3      ...  \n",
      "4  0       9.5\\n1       9.5\\n2       9.4\\n3      ...  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "print(pd.__version__)\n",
    "df_filme_serie['averageRating_and_numVotes']=str(df_filme_serie['averageRating'])+'-'+str(df_filme_serie['numVotes'])\n",
    "print(df_filme_serie.head())  # Exibe as primeiras linhas"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
