# this script is trying to find non-NaN/NaN numbers for specific variable in the nc file
#

find_nan <- function (
nc_var="temp_sol",
nc_file="/ccc/store/cont003/dsm/cheny/Restart_RGRID/ASPINd/SRF/Restart/ASPINd_15471231_sechiba_rest.nc") {

print("Land-point from rgrid map should be 8049.")
# load netcdf library
library(ncdf)
nc_file  <- open.ncdf(nc_file)
var_temp <- get.var.ncdf(nc_file,nc_var)
Non_NaN_numbers     <- sum(!is.na(var_temp))
NaN_numbers         <- sum( is.na(var_temp))

print(paste("Non-NaN-Numbers:",Non_NaN_numbers, "NaN-Numbers:", NaN_numbers))

close.ncdf(nc_file)

}
 
