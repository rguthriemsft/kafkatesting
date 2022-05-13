@description('The name of the HDInsight cluster to create.')
param clusterName string

@description('These credentials can be used to submit jobs to the cluster and to log into cluster dashboards.')
param clusterLoginUserName string = 'admin'

@description('The password must be at least 10 characters in length and must contain at least one digit, one non-alphanumeric character, and one upper or lower case letter.')
@secure()
param clusterLoginPassword string

@description('The location where all azure resources will be deployed.')
param location string = 'westus3'

@description('HDInsight cluster version.')
param clusterVersion string = '4.0'

@description('The number of nodes in the HDInsight cluster.')
param clusterWorkerNodeCount int = 3

@description('The number of zookeeper nodes in the HDInsight cluster.')
param clusterZookeeperNodeCount int = 3

@description('The type of the HDInsight cluster to create.')
param clusterKind string = 'KAFKA'

@description('These credentials can be used to remotely access the cluster.')
param sshUserName string = 'sshuser'

@description('The password must be at least 10 characters in length and must contain at least one digit, one non-alphanumeric character, and one upper or lower case letter.')
@secure()
param sshPassword string
param minTlsVersionNumber string

resource clusterName_resource 'Microsoft.HDInsight/clusters@2015-03-01-preview' = {
  name: clusterName
  location: location
  tags: {}
  zones: null
  properties: {
    clusterVersion: clusterVersion
    osType: 'Linux'
    tier: 'Standard'
    clusterDefinition: {
      kind: clusterKind
      componentVersion: {
        Kafka: '2.4'
      }
      configurations: {
        gateway: {
          'restAuthCredential.isEnabled': true
          'restAuthCredential.username': clusterLoginUserName
          'restAuthCredential.password': clusterLoginPassword
        }
      }
    }
    storageProfile: {
      storageaccounts: [
        {
          name: 'kafkahdinsighhdistorage.blob.core.windows.net'
          isDefault: true
          container: 'kafkahdinsight-2022-05-10t20-43-25-341z'
          key: listKeys('Microsoft.Storage/storageAccounts/kafkahdinsighhdistorage', '2015-05-01-preview').key1
          resourceId: '/subscriptions/ed2c4253-6227-43ef-97e3-4a5fff36888e/resourceGroups/twohat/providers/Microsoft.Storage/storageAccounts/kafkahdinsighhdistorage'
        }
      ]
    }
    computeProfile: {
      roles: [
        {
          autoscale: null
          name: 'headnode'
          minInstanceCount: 1
          targetInstanceCount: 2
          hardwareProfile: {
            vmSize: 'Standard_E4_V3'
          }
          osProfile: {
            linuxOperatingSystemProfile: {
              username: sshUserName
              password: sshPassword
            }
            windowsOperatingSystemProfile: null
          }
          virtualNetworkProfile: null
          scriptActions: []
          dataDisksGroups: null
        }
        {
          autoscale: null
          name: 'workernode'
          targetInstanceCount: clusterWorkerNodeCount
          hardwareProfile: {
            vmSize: 'Standard_E4_V3'
          }
          osProfile: {
            linuxOperatingSystemProfile: {
              username: sshUserName
              password: sshPassword
            }
            windowsOperatingSystemProfile: null
          }
          virtualNetworkProfile: null
          scriptActions: []
          dataDisksGroups: [
            {
              disksPerNode: 2
            }
          ]
        }
        {
          autoscale: null
          name: 'zookeepernode'
          minInstanceCount: 1
          targetInstanceCount: clusterZookeeperNodeCount
          hardwareProfile: {
            vmSize: 'Standard_A4_V2'
          }
          osProfile: {
            linuxOperatingSystemProfile: {
              username: sshUserName
              password: sshPassword
            }
            windowsOperatingSystemProfile: null
          }
          virtualNetworkProfile: null
          scriptActions: []
          dataDisksGroups: null
        }
      ]
    }
    minSupportedTlsVersion: minTlsVersionNumber
  }
  dependsOn: [
    kafkahdinsighhdistorage
  ]
}

resource kafkahdinsighhdistorage 'Microsoft.Storage/storageAccounts@2015-05-01-preview' = {
  name: 'kafkahdinsighhdistorage'
  location: 'westus3'
  properties: {
    accountType: 'Standard_LRS'
  }
}
