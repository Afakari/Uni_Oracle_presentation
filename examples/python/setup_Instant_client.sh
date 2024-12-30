
LINKS=(
    "https://github.com/f00b4r/oracle-instantclient/raw/refs/heads/master/instantclient-basic-linux.x64-12.2.0.1.0.zip"
    "https://github.com/f00b4r/oracle-instantclient/raw/refs/heads/master/instantclient-sdk-linux.x64-12.2.0.1.0.zip"	
	"https://github.com/f00b4r/oracle-instantclient/raw/refs/heads/master/instantclient-sqlplus-linux.x64-12.2.0.1.0.zip"
)

INSTALL_DIR="/usr/lib/oracle"
START_DIR="/tmp/oracle_files"
if [ ! -d "$INSTALL_DIR" ]; then
	mkdir -p "$INSTALL_DIR"
fi


cd $START_DIR

for LINK in "${LINKS[@]}"; do
	wget "$LINK"	
done

for FILE in *.zip; do
	unzip "$FILE"
done

mv instantclient_12_2/* "$INSTALL_DIR"

cd "$INSTALL_DIR"
ln -s libclntsh.so.12.1 libclntsh.so
ln -s libocci.so.12.1 libocci.so

export ORACLE_HOME="$INSTALL_DIR/instantclient_12_2"
echo "export ORACLE_HOME=$INSTALL_DIR/instantclient_12_2" >> ~/.bashrc

export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH
echo "export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH" >> ~/.bashrc

sh -c "echo $ORACLE_HOME > /etc/ld.so.conf.d/oracle-instantclient.conf"
ldconfig



rm -rf "$START_DIR"

echo "Oracle Instant Client and SQL*Plus SDK setup complete."
