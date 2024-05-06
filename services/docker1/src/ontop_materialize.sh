cd "$(dirname "$0")"

echo "Working with full.ttl"
echo $PATH
ontop materialize -m /app/data/full.ttl -p /app/data/ontobridge.properties -o rdf_output.ttl -f turtle

echo "finished"

