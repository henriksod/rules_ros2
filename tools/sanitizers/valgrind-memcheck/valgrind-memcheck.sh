valgrind --leak-check=full --show-leak-kinds=all --error-exitcode=1 --num-callers=30 "${@}"
# --suppressions=tools/sanitizers/valgrind-memcheck/valgrind-suppressions.txt
