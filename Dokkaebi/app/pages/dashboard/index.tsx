import React from 'react';
import { Image, StyleSheet, Text, View, TouchableOpacity, ScrollView, FlatList } from 'react-native';
import { Href, router } from 'expo-router';
import {
  Smartphone,
  Zap,
  Users,
  Settings,
  Cpu,
  FileText,
  Database,
  AlertCircle
} from 'lucide-react-native';

// Estrutura das opções do menu
const options = [
  { id: '1', title: 'Dispositivos', icon: Smartphone, route: '/pages/devices', critical: false },
  { id: '2', title: 'Ações', icon: Zap, route: '/pages/actions', critical: false },
  { id: '3', title: 'Usuários', icon: Users, route: '/pages/users', critical: false },
  { id: '4', title: 'Agentes', icon: Cpu, route: '/pages/agents', critical: false },
  { id: '5', title: 'Logs', icon: FileText, route: '/pages/logs', critical: false },
  { id: '6', title: 'Banco de Dados', icon: Database, route: '/pages/database', critical: false },
  { id: '7', title: 'Configurações', icon: Settings, route: '/pages/settings', critical: false },
];

export default function Dashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dokkaebi</Text>
      <ScrollView>
        <FlatList
        style={styles.grid}
          data={options}
          renderItem={(option) => {
            return (
              <TouchableOpacity style={styles.menuItem}>
                <option.item.icon size={32} color="aqua" strokeWidth={1.5} />
                <Text style={styles.card_title}>{option.item.title}</Text>
              </TouchableOpacity >
            )
          }}
          keyExtractor={option => option.id}
          numColumns={2}
          columnWrapperStyle={styles.row}
        />
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f0f',
    paddingTop: 60,
    paddingHorizontal: 15,
  },
  menuItem: {
    width: '25%',
    aspectRatio: 1.25,
    backgroundColor: '#1a1a1a',
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#252525',
    position: 'relative',
  },
  title: {
    marginTop: 10,
    fontSize: 22,
    fontWeight: '800',
    color: 'white',
    letterSpacing: 4,
    textTransform: 'uppercase',
    textAlign: 'left',
    marginBottom: 30,
    marginLeft: '15%',
    borderLeftWidth: 3,
    borderLeftColor: 'aqua',
    paddingLeft: 15,
  },
  card_title: {
    color: '#e0e0e0',
    marginTop: 12,
    fontSize: 14,
    fontWeight: '600',
    textAlign: 'center',
  },
  row: {
    columnGap: '3vh',
    justifyContent: 'center',
    marginBottom: 16
  },
  grid:{
    width: '100%',
    alignContent: 'center'
  }
});