# mode.R
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
nums = as.numeric(myArgs)

# cat will write the result to the stdout stream
uninums <- unique(nums)
cat(uninums[which.max(tabulate(match(nums, uninums)))])
