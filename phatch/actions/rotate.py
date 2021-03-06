# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.

# Embedded icon is taken from www.openclipart.org (public domain)

# Follows PEP8

from core import models
from lib.reverse_translation import _t
from lib.colors import HTMLColorToRGBA

#---PIL


def init():
    global Image, imtools
    from PIL import Image
    from lib import imtools


def rotate(image, angle, resample_image, expand=0, amount=100,
        background_color='#000000', background_opacity=100):
    resample_image = getattr(Image, resample_image)
    if background_opacity != 100 or background_color != '#000000':
        image = image.convert('RGBA')
    rotated = image.rotate(angle, resample_image, expand)
    rgba = HTMLColorToRGBA(background_color,
                    255 * background_opacity / 100)
    rotated = imtools.fill_background_color(rotated, rgba)
    if amount < 100:
        rotated = imtools.blend(image, rotated, amount / 100.0, rgba)
    return rotated

#---Phatch


class Action(models.Action):
    label = _t('Rotate')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(rotate)
    version = '0.1'
    tags = [_t('transform')]
    __doc__ = _t('Rotate with random angle')

    def interface(self, fields):
        fields[_t('Angle')] = self.SliderField(45, 1, 360)
        fields[_t('Resample Image')] = self.ImageFilterField('bicubic')
        fields[_t('Expand')] = self.BooleanField(False)
        fields[_t('Amount')] = self.SliderField(100, 1, 100)
        fields[_t('Background Color')] = self.ColorField('#000000')
        fields[_t('Background Opacity')] = self.SliderField(0, 0, 100)

    icon = \
'x\xda\x01@\x0b\xbf\xf4\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\n\xf7IDATh\x81\xed\x99m\x8c\x1d\xd5y\xc7\x7f\xcf\x99\
\xb9w\xef\xeezw\xbd\xce\xda\xb0^c\xc7l\x08\xb6\xc161n\x1b\xa3*\xae\xab\x00J\
\xa2 \xd2\n\')ICA\xaa*\xd4~\xaa\x14\x89\xe4CD\xa3$\x9f"Um\xbfF\n\x04\x81\x15\
5\xcd\xabDx\x89bp\x9c\xa4\xd4@l\x821-\xb6\xb1\x89\xbd\xb6\xd7/\xec\xdb\xbdwf\
\xce9O>\xcc\x99\xd9{w\xef\xae\xd7`\x95F\xeaH\x8f\xce\xcc\xdc\x99s\xfe\xff\
\xe7\xfd\xcc\x15U\xe5\x0f\xf90\xef5\x80w{\xfc?\x81\xf7\xfa\xf8\x83\'\x10_\
\xcd\xc9\xb6\x7f\xa1\xb9\xd6*;\x113\x82\xea\xb0\x08\xab\x01T9\x8d\xc8\x18\
\xeaO\xc5\xc2s\x07\x1e\xa9\x9d\xbcZk\xca\xbb\xcdB\x9b\xefKF#\xe4\xb3\xa0\x9f\
\xea\xae\xb2\xad\xbfW\x18\xe8\x85\xfe^a`Y\xfe\xcc\xc44L\xce(\x133\xf9\xd8Hy\
\t\xe4\xfb\x0e}\xe2\x95ow\x1d}O\x08l\xff|}\xd8\x9a\xe8+"<\xb0f\xa5\xc4\x9b\
\xd6\x0b\xbd\xddBd@$\x17#\xf9\xb3\xaa\xe0\x15Pp\x1ef\x9a\xca\xab\xc7\x95\xdf\
\x9dS\xab\xca\xb7b\xef\x1e>\xf0\x9d\x9e\xb1\xff\x15\x02"\xc8\xd6/\xa4_F\xf5\
\xa1\xc1>\xe9\xd9<*\x0c\r\x08Q\x04\xc6@$\xf9h\x0c\xd4\xaa\x90\xa4\xf9{>\x90\
\xf0>\'\xe1\x1c\x9c\x9fP^9\xaa\\\x9c\xd4:"\xdf8\xf8H\xf5k\xaa\\\x11\xa0+"\
\xb0\xf5\xaf\xe9\x15\x93<V\x89\xb8\xfb\xe6\xeb\rkV\tq\x04q\x04\x91\x81(\x828\
\x8c\xc6\xc0G\xb7585\x1es\xe4\xad\n\xde\xe7\x04\n\xf0\xd6\x83\xb5\xf9\xf5[g\
\x95CG=\x99\xe3\x07\xea\xbb>w\xf0Qf\x96\x8ai\xc9Yh\xf3\xfd\x8d\xebD\x92\xfd\
\x91\xe1\xeem7\x1aV\x0fI\xe9*"9\x81\x02|\x1cA%\x12\xd4\xc3\x8e\x9b\x95\x0foJ\
\xa8TZ\xc8F\xb9\xa5\xa2`\xa9\x91U\xc2\x1fm4D\x86\xbbE\x92\xfd\x9b\xefo\\wU\t\
lx\x80\xbe\xc8\x99\'E\xd8\xbae\xd4\xb0<\x04\xa7\x14"\xb3\x17&Hd \xc9\x04c\
\x0c\x1b\xd7\t\xbb\xb66\x88\xe3\xfc7\x11\x10\x13$\xbc:\xd8\'\xdcr\x83A\x84\
\xad\x913Onx\x80\xbe\xabB@\x1e\xc6\xd4l\xf2\x04p\xd3\xb5\xef\x13\x06\xfb\xf2\
\xa0\xd4\xe0\xacJ~]\\x\x85Z\x97\xb0~\xd8\xb2b`v\xfa\x91\x95p\xc7\xadu*\xb1\
\x96\xcf\xce\xf5\xde\xa1\x01X=$\x007\xd5l\xf2\x84<|y|\x97\xad\x03\xb7\x1ck~U\
\x91OD\x11\xac\x1f\x966\xd0\xeaAM~\xbez\xc8\xb1s\xabc\xb0?\xa6Z1\xa8\n\xde\
\x9b\x9ch\x90\x15}\xca\xc7\xffx\x9a\x9f\xfeW\x0f\x17\xa7\xa2\x92\x84/\x14\
\xa2\xf0\x815\xc2\xd9\x8b\x8au|\xe2\x96c\xcd\xafB\xed\xcb\x8b*x\xb1 \xde\xf2\
@r\xbd\xc9\xfc\x11\xa0\xb2jP\xb8\xe1:\xd3\xe6\xc7q\x04\x95\x18>\xf6\')\xdb7v\
c\x8c\x94`\x9ds\xa8*\xde\xfb6q\xceQoz\x9e\xd8\xdbO3\x11\x9cW2\xdb\x12\xdcN9r\
\xc23vAA\xc9\xb4\x1ao8\xf4\xad\xaec\xef\xc8\x02\x92%_W\x95\n\xc0\xf2>\x83sJH\
\xed\xa8\xc2P\xbf\xf2\xf9;\x95\x95+jD\x91\t\xf7s\x02\xad\xe7\xad\xe2\x9c\xf2\
\xabW#\x1a\r\x8f\xf3`]\x9eZ\xbd\x07g\x15\xe7sK\x8d\x8d;\x80\x8a\xa4\xf6\x1b\
\xd0\xf5\xe9\x850.\xe8c[\xee\x9d\xb8U\xbd\xdf\xad\xeaPo\xe9\x8a=\xd6Z2\xeb\
\xb0\xd6Q\x89-\x7f{\x97gh\xb0\x8aHN\xcb{_\x02\xb5\xd6Ro\xa4\xe5=\xef=i\xe6x\
\xf2?\r\xaf\x1c\xef"\xb5\xbe\x9c+\x0bb\x9d\xc3:O\xad\xeaQu\x84\xb5\xef\xd9r\
\xef\xc4\xadWn\x01\xcd\xee#(\xdc\x08\xa8\x172+xU\xbc\x17>\xbd\xcbR\xeb\xea-\
\x01\x17\xee\xf1\x9b#\x93\x1c|Cxk<\xe6\xb6\x9b\x1d\xb7m\x16\xbc\xf74\x13\xcb\
\xf7\x9f7\x9c\x1c\x8fQu\xa1.(\xce\x85\xfa\xe0\xb4\xac\x0f\xea\x15\xc1\xe2}\
\xee\x08\x82\xfb\x1b\xe0\xc5+"\xa0j\xefj\xb5SfC\xd0za\xdbF\xcf\x8d\xebzKW\
\xf1\xde\xf3\xf6d\x83=O\xa7\x1c?\x13\xe7-\x84xj\x15\x87\xf7\x86\xa9\xe9\x84=\
?3\x9c\xb9dr\xf0E\xf0zp^\xcb\xea\xec\xbd\x96n\x05\xae\xccR\x8a~\x12\xf8\xfb%\
\x13\xd8\xb2{l\x9b\x8a_[\\[\x0fif\xd0\x08\xaa\x15\xe1/w\xc5\xf9\xb4\x9a\x83\
\xaf\xd7S\xbe\xfeHB\x92\x1a\xc4\xb8\xb26Tc\xc7\xa5\t\xcf\xb7\x9f\x14.N\x99\
\xe0\x16!\x8b\xf9\xa2\xb5\xd0P\xa1\xb5$d-8k[!\xad\xdd\xb2{l\xdb\xa1\xef\x0e\
\xbf\xb4$\x02\x9e\xec\x8e\xb9\xd9\xa9\xde\x84ZU\xf8\xf0&GO\xad\x1f\xef=\xc6\
\x18\x9cs<\xf2\x93I\xde\x9e\x8c\x11\xe3C\xa1\x12\x04\x18;o\xf9\xf7\x9fGL7\r\
\xaa6Xv6e\xfa0\xba\xe06.\x04s#\xf1\xa8o#\x80\x13w\'\xb04\x02\xa8[\x87\xfa\
\xb6[SS\x9e\xa8/b\xfd\xb5\xb9\xd6\x8b\xe3\xb5cS\xfc\xfa0D\x85\xe6\r\x80""\
\xfc\xf0\x17\x02\xf8 t P\xb8\x92\xe6\xf1\xe0s\xcb\\\x9a\xb2\xa8\xba\xb6\xf5E\
e]\'\xa8\x1d\t\xa8\xcfF\xe66\x85\xd3u\xa1\xa7\xa6\x8c\xac\xaa\x94A\x0bp\xf0\
\x7fR\xd24\x07n$\xf4G\x00\xa1e@s2\x05\xe8|\x81\xdc\x8d\x8a@.\xda\xec<A\xc0\
\xd4T\x1a\xfa\xefV\x06fd\xc9\x04\xbc\xfa\xd5\xadZ\x83<\x88\'\xa7=\xab\x06km\
\xee\xf3\xf2\x91\x8c$\x95\x10\xb8\xc5> \'B\x87\xceX\x83\xd65\xc4P\x19\x0b\
\xaa\xa8\x87\x99\x86\'\xcd\xec\xbc\xf7\xbc\xea\xea%\x13\x80\xack\x9e\x06\x00\
<tU\x05\xe7\\\xb0\x80\xf0\xfaI\x8bj\xd8\x03\x84\xe8\re\xa1,z-\xf0\xdbz\'U-\
\xddHU\xb1\x0e.Mf\xf3z\xa4|2\xe9Z2\x01\xf5\xee\x0c\xeao\x9e{\x7fr\x06&\xa6\
\x12\x06\xfa\xba\xf2@\x15a\xcdJ\xc7\x1b\xbfS\x0c\x9ak?l\xc3d>\xfa\xd9\xf9\
\x03\xe0\xdb\xb7[\x86\x06,\xd6z\xb2\xcc\xf2\xd4\x0b\x15\xc6]\xd4\xf9%\x13\
\x9dY2\x01Q?\xe6\xfd|3\x02\x9c8]g\xd3h\x841y\x11\xff\xe0\x1a\xe5\xf0\xd1\xa4\
\xd4\xbc\xd0B\xa2\x13\xf80F\x06vlj\x10\x1b\x8bs\x8e$Ix\xfc\xd9\x01\x16\xea\
\xcd\xc4\xcb\xe9%\x13\xf0\xca)\xd4\xd1iw\xf7\xdf\'\x126\xac\xef-\x83\xf8\xa6\
\xd1\x98=\xcf\xcc\x84\x0c$\x08\xb3\xfdR\'+\x14\xf8nZ\xaf\xc4\xc6\xe6\xedI\
\x961vA\x98\x98V\xa0\xc8>\xedk\xab1\x1d\tt\xec\x85D\xec>UW\x94\xdeY\xf1\x8eW\
\x8f&m\xdd\xe5\xe6\xd1.\xb6\xdf(\xa4IF\xda\xccH\x92\x8cf3\xa5\x994i4\x1a\xb3\
\xd2l\xd2h&$IJ\xe62v}(%\xcb2\xac\xcd-\xf0\xda\x89\xa2\xd0\xd9 \xaeMD\xdc\xbe\
NX;Z`\xd9\xa9\xe8\x99\x89Uv\x12\xa5\x7f\xae&\xf6\xfd\xc6r\xdf\xf9:C\x83\xb31\
\xf5\xe0=\x03\xbc|\xe4\x14\xd3u\x8b\xb6\x12n{wv\xff\xf9W;k\xbc\xff\x1ap\xce\
\x97\xcd\xde\xe17\x05t\x8e\xdb\x16\xe6\x12\x99\xec;]}z\xc9\x168p\xe0\xd6\x0c\
\xcc\xdeN\x9aH\x12\xcb7\x1f=\x87\xb5\xael\xe0\xfaz\xe0\x9f\xffq%\x9b\xd6y|6\
\x83\xcf\xa6qvf\x9eT\xa4\xce\xee]\x11\x7f\xf6!)\xdfu\xceq\xe0\x88\xe1\xf5\
\x93\x8az\xdb.aM\x90\xbd9\xa6%Z\x00@\x91\xc7\xf1-\r]\xcb\xf1\xf2\xeb\x8e\xa7\
\xf6\x9f\xe7\x8e\xdbV\x94\xdd\xe8\xd0r\xc3?=8\xc2O\xf7\x8f\xb3\xef\xc5K\xbc~\
|\x8a4\xf3\x88(+\x06\xaal\xba\xbe\x87O\xfd\xf9 +\xfa\xa5\x04\xee\xbdg\xfc\
\x92\xb2\xe7\xd9&\xde\xc5\x88Y\x08N\xf5\xf1\x85p.\xba#\x1b\xbd\xe3\xa9Ch\xb6\
y\x1e9uT\x8c\xe3\xdf\x1e\xba\x8ek\x87jm\x1b\x96"6\xd2\xccs\xfa\xec\x0c\xcbzb\
z\xbbi\xd3x!\xd6*\xdf|l\x92\x93\xe7<b*\x88\x14$Z\xa2\xdfT~{\xf4\xe9\x8f\xcd\
\xc3P\xfe\xbc z\x80(\xfe\xd2<\xb3\xba\x14\xb5M\x92\xa4\xce?|\xed5\x9e{\xe1L\
\xa9\xcdVpF<\xc3+\xab\xf3\xc0\x17\x04\xc7/\xa6\xfc\xeb\x9e3\xbcyj\x12u\t\xde\
5\x83$-\x81l\xc1\xc4\x0f-\x06\xf1\xb2\x1f\xb6\xae\xbf\xfd\'\xcf\xe1\x92\x8f\
\x14\xdf r"i\x183T3vl\xe9\xe7\xef>\xf3\x01\xfaz+,\xb4\x0f.\xc0g\xd6\xf1\xf4\
\xfe\xb3\xfch\xef8\x995\x88\x89\x83\xe6+`*\xe1:\x8c\xa6\xeb\xf9c\xcf\xde\xb5\
s1|\x97\xfd*ad\xf0\x1e\xc7\xd8K\xa8\x1b\xc9\x03+\xcb\xad\xe03\xd4g\xe0-\xbf|\
\xf14\x87\x0e\x8fq\xe7\x9f^\xcb\xe8\xba~\xd6\x0e/c\xc5\xf2\xae\x92L\xbd\x91r\
\xe2\xd4\x04\xc7NN\xf2\x8b\x17\xcfqr\xac\x01\x12\xe5\xa0}\x0c&\x06u\x88:\xd0\
\n\x18\x0f\x12\x9fB{v_\x0e\xdf\x92>-\x8e\xde\xfe\xd46\x97]x^]\xd2;\xab\xfd\
\xd61\x0b\xd6\xb0\x10\xb2\xc7\xb2n\xc3\xba\x91~.\xbc]\xe7\xcc\xf84\xaa\x82H\
\x04&B\xc4\x94Z\xce\xb5\xde\xaa\xf9\n&\xee\x9f\x89k\xd7|\xe4\xe83w\xce\xeb\
\xff\xdf\x11\x81\x9c\xc4\x8f\xff\xc26\xc6\x1f\xf3\xae\xde]\x02.\xfc\xd5\xa5\
\xf9\xe8\xb3\x90\xfe,\x14)\xb0\xcc\xe5&\x00\xcf5>\x1b\xb4\x9561\xd5\xfeF\xb5\
g\xe4sG\x9f\xf9\xe4\x7f,\x05\xd7\x15}\xdc\x1d\xfd\xe8\x0fw\xa43\xa7\x7f\xe0\
\xed\xd4\xaa\x92D)i\x0b\x81\xe0^\xea\xf2\xc2\x86\xe4\xe0M\x0csAK\x8cDUD*D\
\xd5\x81\xf3\x95\x9e\xe1\xbb\xdf\xdc\xfb\x99_\xa9\xce\xd9Q\xbd\x1b\x02"b\x80\
\x08\xa8^\xb3\xf1\xc1uq\xdf\r\xdfs\xe9\xc4\x86\x02\xe8,\x81\xdc\xa5h%\x96\
\x17"\xc4D\x01pe\x9e\xd6\xc5T1\xd5\xfe7\xb2\x8b\x07?{\xfe\xf8w\xdf\x04\x9a@\
\nX@u\x11\x90\x8b\x12\x08\xc0\rP\x05\xba\x80\x9e \xbd\xab6\x7f\xf1^\x13u\xdf\
\xef\xb2\xa9\x15\xcc\xb5\x86\xb6_\xe7\x04:\x01\x8f\x89\xaa\xcb\'\x9c\xad\x7f\
\xe7\xfc\xe1\x7f\xd9\x03\xcc\x00\xf506Z\x88\xf8\x85,\xb2 \x01\xc9\xbfVE\x01x\
\r\xe8\r\xb2\xac\x18\xa3\xa8\xbb\x7f\xf0\x83\xf7\xef\x16S\xdd\xe1mc%\x9a\xc9\
,\xf0\xd9X\xc8\xe7\x0b\xbe\x9f\x07\xaf\x9a\xb8\xf7\x82\xaa}\xe1\xed7\x1e\xfd\
\x9es\xcd\xc9\x00z\xbaE\n"M \xd3\xb9\x9b\xe4%\x100@\xa5E\xf3\xcbZ\xa4\xaf\
\xe5\xbc\x17XV\xa9]3\xd2;\xbcs{\\\x1dZ\x0b\xae\xd7\xfb\xac\xa6.\x89\xc1\x8b\
\x98J&\xa6\x9a\x80\xcc\xb8\xe4\xe2[3g\xf7\xbd\x945\xcf\x9d\x9e\x03\xb8\x90\
\xa9\x96\xb1^X\xe1\x9d\x10h\xb5@w\x07\xf0}\x1d\xac\xd2\x13\xac\xd5\x1d\xde+\
\xb6W\x0eH\x82\xd4[\xb4[\xc8\\\xe0\xc5y\x9dY\x17\xea\x08t\x91/s\xaa\x80\x15\
\x11O\x1eLY\x07)@5\xc2\x82\xb5\x00\xbc\x1a\xc0\x1b\xca\x7f\x03\xb0\xe1\xd94<\
\xdfJ\xa4\xd0\xfe\xe4\x1c\xe0\xeer\xd9h\xc9i4\xb8\x94\x04\xd2Ur-\x17\xae\xd5\
Cn\x81Z\xf8\xad\x12\x08H\x00_(!%w\x89\x82@\x01\xb6\x00\x9c\x91[k\xd1\xcc\xf3\
\x8e\x08\xcc!\xd3\xf2\xa7R\xbe\r\xee0\x16\xe7\x85\x05|\x8b\xb4\xde\xd3+\x01|\
U\x08\xfc_:~\x0f\xbc\xd1\xbd\'X\xe0\x9fO\x00\x00\x00\x00IEND\xaeB`\x82Ex\xa6\
X'
