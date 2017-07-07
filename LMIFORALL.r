library(jsonlite)
library(DT)
library(RCurl)


json_file <- paste0("http://api.lmiforall.org.uk/api/v1/vacancies/search?keywords=",'Cook')
result <-data.frame(jsonlite::fromJSON((json_file)))



datatable(result)




result

