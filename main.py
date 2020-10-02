import PySimpleGUI as sg
import ems

sg.theme('Default1')

column_1 = [
    [sg.Input(key='-QUERY-', size=(30, 1))],
    [sg.Text('Minimum Sell Price')],
    [sg.Text(size=(15, 1), key='-SELLPRICE-')],
    [sg.Text('Maximum Buy Price')],
    [sg.Text(size=(15, 1), key='-BUYPRICE-')],
]

column_2 = [
    [sg.InputCombo(('Jita', 'Amarr', 'Dodixie', 'Rens', 'Hek'), size=(10, 1), default_value='Jita', key="-HUB-")],
    [sg.Text('Quantity (Total)')],
    [sg.Text(size=(15, 1), key='-SELLQUANTITY-')],
    [sg.Text('Quantity (Total)')],
    [sg.Text(size=(15, 1), key='-BUYQUANTITY-')],
]

column_3 = [
    [sg.Button('Search', bind_return_key=True)],
    [sg.Text('Orders')],
    [sg.Text(size=(15, 1), key='-SELLORDERS-')],
    [sg.Text('Orders')],
    [sg.Text(size=(15, 1), key='-BUYORDERS-')],
]

layout = [
    [
        sg.Column(column_1, justification='right'),
        sg.Column(column_2, justification='right'),
        sg.Column(column_3, justification='right'),
    ]
]
window = sg.Window('GEMS', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Search':
        item_id = ems.lookup_item_id(values['-QUERY-'])
        if item_id == None:
            sg.popup('Item not found.', modal=True)
            continue
        hub = ems.determine_system(values['-HUB-'])
        market_info = ems.search_market(item_id, hub)
        window['-SELLPRICE-'].update(market_info['min_sell'] + ' ISK')
        window['-BUYPRICE-'].update(market_info['max_buy'] + ' ISK')
        window['-SELLQUANTITY-'].update(market_info['sell_volume'])
        window['-BUYQUANTITY-'].update(market_info['buy_volume'])
        window['-SELLORDERS-'].update(market_info['sell_orders'])
        window['-BUYORDERS-'].update(market_info['buy_orders'])

window.close()
