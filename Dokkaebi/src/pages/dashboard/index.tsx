import { HeaderTitle } from '@react-navigation/elements';
import { Button, StyleSheet, View } from 'react-native';

export type Props = {
  name: string;
};

function DashBoard({ name }: Props) {


  return (
    <View style={styles.container}>
      <View style={styles.menu}>
        <HeaderTitle>Dispositivos</HeaderTitle>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  menu: {
    fontSize: 20,
    fontWeight: 'bold',
    margin: 16,
  },
});

export default DashBoard;