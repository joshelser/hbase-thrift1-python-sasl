#!/usr/bin/env python

# Copyright 2017 Josh Elser
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from hbase_thrift.hbase import Hbase

# Apache HBase Thrift server coordinates (network location)
thriftServer = "hw10447.local"
thriftPort = 9090
# The service name is the "primary" component of the Kerberos principal the
# Thrift server uses. 
# See: http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html
# e.g. For a server principal of 'hbase/localhost@EXAMPLE.COM', the primary is "hbase"
saslServiceName = "hbase"

# HBase table and data information
tableName = "FOOBAR"
row = 'r1'
colName = "f1:cq1"

# Open a socket to the server
sock = TSocket.TSocket(thriftServer, thriftPort)
# Set up a SASL transport. 
transport = TTransport.TSaslClientTransport(sock, thriftServer, saslServiceName)
# Use the Binary protocol (must match your Thrift server's expected protocol)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Pass the above to the generated HBase clietn
client = Hbase.Client(protocol)
transport.open()

# Fetch a row from HBase
print "Row=>%s" % (client.getRow(tableName, row, {}))

# Cleanup
transport.close() 
