# installer for wh2900 extension
# Compatible with WeeWX 4.x and 5.x

from weecfg.extension import ExtensionInstaller


def loader():
    return WH2900Installer()


class WH2900Installer(ExtensionInstaller):
    def __init__(self):
        super(WH2900Installer, self).__init__(
            version="0.1",
            name='wh2900',
            description='WH2900 custom skin and user extensions',
            author='David Blaik',
            author_email='blaikey@outlook.com',
            files=[
                # User extensions
                ('bin/user', [
                    'bin/user/since.py',
                    'bin/user/time_since.py'
                ]),

                # Skin root
                ('skins/wh2900', [
                    'skins/wh2900/index.html.tmpl',
                    'skins/wh2900/skin.conf'
                    'skins/wh2900/manifest.json'
                    'skins/wh2900/sw.js'
                ]),

                # Skin CSS
                ('skins/wh2900/css', [
                    'skins/wh2900/css/wh2900.css'
                ]),

                # Weather icons
                ('skins/wh2900/icons', [
                    'skins/wh2900/icons/clear.svg',
                    'skins/wh2900/icons/clear-night.svg',
                    'skins/wh2900/icons/cloudy.svg',
                    'skins/wh2900/icons/cloudy-night.svg',
                    'skins/wh2900/icons/fog.svg',
                    'skins/wh2900/icons/fog-night.svg',
                    'skins/wh2900/icons/mostly-sunny.svg',
                    'skins/wh2900/icons/partly-cloudy.svg',
                    'skins/wh2900/icons/partly-cloudy-night.svg',
                    'skins/wh2900/icons/rain.svg',
                    'skins/wh2900/icons/rain-night.svg',
                    'skins/wh2900/icons/snow.svg',
                    'skins/wh2900/icons/snow-mood.svg',
                    'skins/wh2900/icons/storms.svg',
                    'skins/wh2900/icons/storms-night.svg'
                ]),
                
                # fonts
                ('skins/wh2900/fonts/DSEG&-Modern', [
                    'DSEG7Modern-Bold.ttf'
                    'DSEG7Modern-Bold.woff'
                    'DSEG7Modern-Bold.woff2'
                    'DSEG7Modern-BoldItalic.ttf'
                    'DSEG7Modern-BoldItalic.woff'
                    'DSEG7Modern-BoldItalic.woff2'
                    'DSEG7Modern-Italic.ttf'
                    'DSEG7Modern-Italic.woff'
                    'DSEG7Modern-Italic.woff2'
                    'DSEG7Modern-Light.ttf'
                    'DSEG7Modern-Light.woff'
                    'DSEG7Modern-Light.woff2'
                    'DSEG7Modern-LightItalic.ttf'
                    'DSEG7Modern-LightItalic.woff'
                    'DSEG7Modern-LightItalic.woff2'
                    'DSEG7Modern-Regular.ttf'
                    'DSEG7Modern-Regular.woff'
                    'DSEG7Modern-Regular.woff2'                
                ]),

                # Moon phase icons
                ('skins/wh2900/icons/moon', [
                    'skins/wh2900/icons/moon/full-moon.svg',
                    'skins/wh2900/icons/moon/new-moon.svg',
                    'skins/wh2900/icons/moon/waning-crescent.svg',
                    'skins/wh2900/icons/moon/waning-gibbous.svg',
                    'skins/wh2900/icons/moon/waning-quarter.svg',
                    'skins/wh2900/icons/moon/waxing-crescent.svg',
                    'skins/wh2900/icons/moon/waxing-gibbous.svg',
                    'skins/wh2900/icons/moon/waxing-quarter.svg'
                ]),
            ],
            config={
                'StdReport': {
                    'wh2900': {
                        'skin': 'wh2900',
                        'HTML_ROOT': 'wh2900',
                        'enable': 'true'
                    }
                }
            }
        )