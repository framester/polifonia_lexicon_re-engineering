{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('../input/csv_for_rdf/automatic_EN_filtered.csv')\n",
    "enriched_df = pd.read_csv('../input/csv_for_wn_alignment/automatic_en_filtered_aligned_to_wordnet.csv', on_bad_lines='skip')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fill empty values in 'Value' column of df2 with values from df1\n",
    "df['wn_synset'].mask(df['wn_synset'].isna(), enriched_df['wn_synset'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>wn_synset</th>\n",
       "      <th>bn:id</th>\n",
       "      <th>pos</th>\n",
       "      <th>lemmata EN</th>\n",
       "      <th>definition</th>\n",
       "      <th>is it related to music?</th>\n",
       "      <th>note</th>\n",
       "      <th>removed EN</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>wn:15264726n</td>\n",
       "      <td>bn:00000627n</td>\n",
       "      <td>NaN</td>\n",
       "      <td>accelerando</td>\n",
       "      <td>A gradually increasing tempo of music</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>wn:15264726n</td>\n",
       "      <td>bn:00000627n</td>\n",
       "      <td>NaN</td>\n",
       "      <td>halo</td>\n",
       "      <td>A gradually increasing tempo of music</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>wn:15264726n</td>\n",
       "      <td>bn:00000627n</td>\n",
       "      <td>NaN</td>\n",
       "      <td>nightfall</td>\n",
       "      <td>A gradually increasing tempo of music</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>wn:15264726n</td>\n",
       "      <td>bn:00000627n</td>\n",
       "      <td>NaN</td>\n",
       "      <td>accelenrando</td>\n",
       "      <td>A gradually increasing tempo of music</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>wn:15264726n</td>\n",
       "      <td>bn:00000627n</td>\n",
       "      <td>NaN</td>\n",
       "      <td>lobsters</td>\n",
       "      <td>A gradually increasing tempo of music</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20573</th>\n",
       "      <td>wn:01050651v</td>\n",
       "      <td>bn:00086659v</td>\n",
       "      <td>v</td>\n",
       "      <td>descant</td>\n",
       "      <td>sing by changing register; sing by yodeling</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20574</th>\n",
       "      <td>wn:01256124n</td>\n",
       "      <td>bn:00081923n</td>\n",
       "      <td>n</td>\n",
       "      <td>yodeling</td>\n",
       "      <td>singing by changing back and forth between the...</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20575</th>\n",
       "      <td>wn:10803838n</td>\n",
       "      <td>bn:00081924n</td>\n",
       "      <td>n</td>\n",
       "      <td>yodeller</td>\n",
       "      <td>a singer who changes register rapidly (popular...</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20576</th>\n",
       "      <td>wn:04614844n</td>\n",
       "      <td>bn:00082041n</td>\n",
       "      <td>n</td>\n",
       "      <td>zill</td>\n",
       "      <td>one of a pair of small metallic cymbals worn o...</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20577</th>\n",
       "      <td>wn:07062550n</td>\n",
       "      <td>bn:00082108n</td>\n",
       "      <td>n</td>\n",
       "      <td>zydeco</td>\n",
       "      <td>music of southern Louisiana that combines Fren...</td>\n",
       "      <td>YES</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>20578 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          wn_synset         bn:id  pos    lemmata EN  \\\n",
       "0      wn:15264726n  bn:00000627n  NaN   accelerando   \n",
       "1      wn:15264726n  bn:00000627n  NaN          halo   \n",
       "2      wn:15264726n  bn:00000627n  NaN     nightfall   \n",
       "3      wn:15264726n  bn:00000627n  NaN  accelenrando   \n",
       "4      wn:15264726n  bn:00000627n  NaN      lobsters   \n",
       "...             ...           ...  ...           ...   \n",
       "20573  wn:01050651v  bn:00086659v    v       descant   \n",
       "20574  wn:01256124n  bn:00081923n    n      yodeling   \n",
       "20575  wn:10803838n  bn:00081924n    n      yodeller   \n",
       "20576  wn:04614844n  bn:00082041n    n          zill   \n",
       "20577  wn:07062550n  bn:00082108n    n        zydeco   \n",
       "\n",
       "                                              definition  \\\n",
       "0                  A gradually increasing tempo of music   \n",
       "1                  A gradually increasing tempo of music   \n",
       "2                  A gradually increasing tempo of music   \n",
       "3                  A gradually increasing tempo of music   \n",
       "4                  A gradually increasing tempo of music   \n",
       "...                                                  ...   \n",
       "20573        sing by changing register; sing by yodeling   \n",
       "20574  singing by changing back and forth between the...   \n",
       "20575  a singer who changes register rapidly (popular...   \n",
       "20576  one of a pair of small metallic cymbals worn o...   \n",
       "20577  music of southern Louisiana that combines Fren...   \n",
       "\n",
       "      is it related to music? note  removed EN  \n",
       "0                         YES  NaN         NaN  \n",
       "1                         YES  NaN         NaN  \n",
       "2                         YES  NaN         NaN  \n",
       "3                         YES  NaN         NaN  \n",
       "4                         YES  NaN         NaN  \n",
       "...                       ...  ...         ...  \n",
       "20573                     YES  NaN         NaN  \n",
       "20574                     YES  NaN         NaN  \n",
       "20575                     YES  NaN         NaN  \n",
       "20576                     YES  NaN         NaN  \n",
       "20577                     YES  NaN         NaN  \n",
       "\n",
       "[20578 rows x 8 columns]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.tocsv('../input/csv_for_rdf/automatic_EN_filtered.csv', index=False)"
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
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
