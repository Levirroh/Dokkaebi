import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ScrollView } from 'react-native';
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
const MENU_OPTIONS = [
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
      <Text style={styles.brand}>Dokkaebi</Text>
      
      <ScrollView contentContainerStyle={styles.grid}>
        {MENU_OPTIONS.map((card) => (
          <TouchableOpacity 
            key={card.id} 
            style={styles.menuItem}
            onPress={() => router.replace(card.route as Href)}
            activeOpacity={0.7}
          >
            {card.critical && (
              <View style={styles.badge}>
                <AlertCircle size={14} color="#000" strokeWidth={3} />
              </View>
            )}

            <card.icon size={32} color="orange" strokeWidth={1.5} />
            <Text style={styles.menuText}>{card.title}</Text>
          </TouchableOpacity>
        ))}
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
  brand: {
    fontSize: 22,
    fontWeight: '800',
    color: 'white',
    letterSpacing: 4,
    textTransform: 'uppercase',
    textAlign: 'left',
    marginBottom: 30,
    marginLeft: 10,
    borderLeftWidth: 3,
    borderLeftColor: 'orange',
    paddingLeft: 15,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    paddingBottom: 20,
  },
  menuItem: {
    width: '48%', // Garante 2 por linha com espaçamento
    aspectRatio: 1.25, // Mantém o container quadrado
    backgroundColor: '#1a1a1a',
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#252525',
    position: 'relative', // Para o posicionamento do badge
  },
  menuText: {
    color: '#e0e0e0',
    marginTop: 12,
    fontSize: 14,
    fontWeight: '600',
    textAlign: 'center',
  },
  badge: {
    position: 'absolute',
    top: 10,
    right: 10,
    backgroundColor: 'orange',
    borderRadius: 10,
    width: 20,
    height: 20,
    justifyContent: 'center',
    alignItems: 'center',
    // Glow effect para o alerta
    shadowColor: 'orange',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.8,
    shadowRadius: 4,
    elevation: 5,
  },
});