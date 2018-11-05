## Preprocessing rules

### Initial preprocessing:

    * Remove columns that has more than 35% is nan
    * Remove rows that has more than 50% is nan
    * Replace nan with mean for int column and 'no category' for string column

### Medications:

    * Groupby SEQN
    * Only use 'RXDDRGID' (drug_id), store a dict that map 'RXDDRGID' to 'RXDDRUG' (drug_name)
    * Only use 'RXDRSC1' (condition_name), store a dict that map 'RXDRSC1' to 'RXDRSD1' (condition_name)
    * 'RXDUSE', 'RXQSEEN', 'RXDCOUNT' are array of similar number => Use mode
    * Use get_dummies to hot_one_code 'RXDDRGID', replace value with 'RXDDAYS' (days of using)
    * Use get_dummies to hot_one_code 'RXDRSC1'