import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versao: {item.version}.')
    print(f'Data instalacao: {item.install_date}.')
    print(f'publicacao: {item.publisher}.')
    print(f'Local desinstalacao: {item.uninstall_string}.')
    print('-'*50)