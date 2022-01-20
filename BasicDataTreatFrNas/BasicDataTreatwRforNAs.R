#Basic Data Treatment in R for N.A cases

ch_file = choose.files()
n_data = read.csv(ch_file, sep = ";", stringsAsFactors = T)
print(n_data$Temperatura)

data_NaTreat <- function(n_data){
  n_col = NCOL(n_data)
  names_col = colnames(n_data)
  ls = (colnames(n_data))
  n_ls = as.list(strsplit(ls, " ")[])
  
  for (col in n_col) {
    new_col = n_data[,col]
    check_empty = T %in% n_data[is.na(n_data),col]
    
    if (check_empty == TRUE | "" %in% new_col){
      if (is.numeric(n_data$n_ls[col])) {
        n_data[is.na(n_data)$col] = median(n_data$col, na.rm = T)
      }
    }
  }
  return(n_data)
} 

final_data = data_NaTreat(n_data)
print(final_data)
