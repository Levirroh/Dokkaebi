//documento geral e padrão do app, tudo é padronizado por este, ex. fontes, background, etc.

import { DarkTheme, DefaultTheme, ThemeProvider } from '@react-navigation/native';
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import 'react-native-reanimated';

import { useColorScheme } from '@/hooks/use-color-scheme';
import { HeaderShownContext } from '@react-navigation/elements';

export default function RootLayout() {
  const colorScheme = useColorScheme();

  return (
    <ThemeProvider value={colorScheme === 'dark' ? DarkTheme : DefaultTheme}>
      <Stack screenOptions={{ headerShown: false }}> // headerShown: false - faz nao aparecer o caminho no header
      </Stack>
      <StatusBar style="auto" />
    </ThemeProvider>
  );
}
