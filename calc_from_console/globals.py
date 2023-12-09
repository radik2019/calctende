import click


PRINT_WIDTH = 30
INPUT_VARIABLE = {
        'PiegaFissa': [
            # VARIABLES NAME
            ['piega_aprossimata', 'm_dentro', 'misura_tenda', 'misura_stoffa'],

            # INPUT PRINT
            ["m. piega:", "m. dentro:", "m. tenda:", "m. stoffa:"]],

        'PiegaTubolare': [
            ['piega', 'piega_den', 'space', 'm_tend', 'm_stoff'],
            ['piega:',  'piega dentro:', 'spazio tra pieghe:','misura tenda:', 'stoffa:' ]],

        'StoffaPiegaFissa': [['tenda', 'piega', 'piega_dentro'],
            ['tenda:', 'piega:', 'piega dentro:']],
        
        'Onda': [
            ['passo', 'taschini_vuoti', 'binary_type', 'presunta_misura_bin', 'fettuccia'],
            [
            '[>] passo "8" o "6',
            '[>] taschini vuoti tra ganci',
            "[>] binario [1 telo / 2 teli]",
            '[>] misura del binario',
            "[>] fettuccia da [7cm / 9cm]",
        ]]
    }












