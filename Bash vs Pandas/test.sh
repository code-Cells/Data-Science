# Print head
echo "HEAD"
head -5 signals.csv | tail -5
echo ""

# Print tail
echo "TAIL"
tail -5 signals.csv
echo ""

# Print specific line
echo "THIRD LINE"
cat signals.csv | sed -n '3p'
echo ""

# Save and print specific columns to outer file
echo "DESCRIPTION"
cat signals.csv | sed -n '2,$p' | cut -d ';' -f 1,3 > sliced_bash.csv
cat sliced.csv
echo ""

