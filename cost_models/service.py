# import datetime
# import itertools
# from difflib import SequenceMatcher
# from pprint import pprint
# import re
# # from .price import price
# from price.models import Global, Iphone, Markup, Ipad, MacBook1, Watch, SpecialCharacter

# specification = [[i.provider_variant, i.new_variant] for i in SpecialCharacter.objects.all()]

# memory_devices = '16gb|32gb|64gb|128gb|256gb|512gb|1tb|' \
#                  '16гб|32гб|64гб|128гб|256гб|512гб|1тб|' \
#                  '16 gb|32 gb|64 gb|128 gb|256 gb|512 gb|1 tb|' \
#                  '16 гб|32 гб|64 гб|128 гб|256 гб|512 гб|1 тб'

# country_colors = Global.objects.all()[0]
# colors = country_colors.color
# country = country_colors.country

# # iphone
# iphone_all_info = Iphone.objects.all()[0]
# list_iphone = iphone_all_info.series_prefix  # 11 pro, 11 pro max
# iphone_full_names = iphone_all_info.full_name  # iphone 8, iphone x, iphone 11
# iphone_memory = iphone_all_info.memory  # 16, 16гб, 16gb
# iphone_extra_models = iphone_all_info.series_not_prefix  # 6, 7, 8, 11,
# iphone_extra_names = iphone_all_info.extra_iphone  # se, sr, x, xs

# iphone_extra_clear = re.sub('^\s+|\n|\r|\s+$', '', iphone_extra_names).split(',')
# iphone_memory_clear = re.sub('^\s+|\n|\r|\s+$', '', iphone_memory).split(',')
# list_iphone_clear = re.sub('^\s+|\n|\r|\s+$', '', list_iphone).split(',')
# iphone_full_names_clear = re.sub('^\s+|\n|\r|\s+$', '', iphone_full_names).split(',')
# iphone_extra_models_clear = re.sub('^\s+|\n|\r|\s+$', '', iphone_extra_models).split(',')
# iphone_extra = [x[0] + ' ' + x[1] for x in itertools.product(iphone_extra_clear, iphone_memory_clear)]
# iphone_extra2 = [x[0] + ' ' + x[1] for x in itertools.product(iphone_extra_models_clear, iphone_memory_clear)]
# check_names_iphone = list_iphone_clear + iphone_extra + iphone_full_names.split(',') + iphone_extra2
# re_iphone = '|'.join(list_iphone_clear + iphone_extra_clear + iphone_extra_models_clear).replace(' ', '')

# # ipad
# ipad_all_info = Ipad.objects.all()[0]
# ipad_series = ipad_all_info.series  # Pro, Air
# ipad_series_number = ipad_all_info.numbers  # 11, 12.9
# ipad_wifi = ipad_all_info.names

# ipad_series_clear = re.sub('^\s+|\n|\r|\s+$', '', ipad_series).split(',')
# ipad_series_number_clear = re.sub('^\s+|\n|\r|\s+$', '', ipad_series_number).split(',')
# ipad_wifi_clear = re.sub('^\s+|\n|\r|\s+$', '', ipad_wifi).split(',')
# ipad_extra = [x[0] + ' ' + x[1] for x in itertools.product(ipad_series_clear,
#                                                            ipad_series_number_clear)]
# ipad_extra_2 = [x[0] + ' ' + x[1] for x in itertools.product(ipad_series_clear,
#                                                              ipad_wifi_clear)]
# ipad_extra_3 = ['ipad ' + x for x in ipad_series_clear]
# check_names_ipad = ipad_extra + ipad_extra_2 + ipad_extra_3 + ipad_series_number.split(',')

# # MacBook
# macbook_all_info = MacBook1.objects.all()[0]
# macbook_memory = macbook_all_info.memory  # 16, 16гб, 16gb
# macbook_series = macbook_all_info.series  # MacBook, MacBook Pro...')
# macbook_names = macbook_all_info.names  # M1')
# macbook_extra = macbook_all_info.extra  # 'MacBook 11 , MacBook Pro 12')

# macbook_memory_clear = re.sub('^\s+|\n|\r|\s+$', '', macbook_memory).split(',')
# macbook_series_clear = re.sub('^\s+|\n|\r|\s+$', '', macbook_series).split(',')
# macbook_names_clear = re.sub('^\s+|\n|\r|\s+$', '', macbook_names).split(',')
# macbook_extra_clear = re.sub('^\s+|\n|\r|\s+$', '', macbook_extra).split(',')
# macbook_extra_1 = [x[0] + ' ' + x[1] for x in itertools.product(macbook_series_clear,
#                                                                 macbook_names_clear)]
# check_names_macbook = macbook_extra_1 + macbook_extra_clear
# re_macbook_memory = '|'.join(macbook_memory_clear).replace(',', '')

# re_macbook = '|'.join(macbook_extra_clear + macbook_series_clear).replace(' ', '').lower()

# # Watch
# watch_all_info = Watch.objects.all()[0]
# watch_size = watch_all_info.size  # 44mm, 45mm
# watch_size_exists = watch_all_info.size_exists  # 44,45
# watch_series = watch_all_info.series  # 5,6,7...
# watch_series_full_names = watch_all_info.series_full_names  # Series 3, Series 4
# watch_extra = watch_all_info.extra  # SE

# watch_size_clear = re.sub('^\s+|\n|\r|\s+$', '', watch_size).split(',')  # 44mm, 45mm
# watch_size_exists_clear = re.sub('^\s+|\n|\r|\s+$', '', watch_size_exists).split(',')  # 44,45
# watch_series_clear = re.sub('^\s+|\n|\r|\s+$', '', watch_series).split(',')  # 5,6,7...
# watch_series_full_names_clear = re.sub('^\s+|\n|\r|\s+$', '', watch_series_full_names).split(',')  # Series 3, Series 4
# watch_extra_clear = re.sub('^\s+|\n|\r|\s+$', '', watch_extra).split(',')  # SE

# watch_extra_1 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_clear,
#                                                               watch_size_clear)]
# watch_extra_2 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_clear,
#                                                               watch_size_exists_clear)]
# watch_extra_3 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_full_names_clear,
#                                                               watch_size_clear)]
# watch_extra_4 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_full_names_clear,
#                                                               watch_size_exists_clear)]
# watch_extra_5 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_full_names_clear,
#                                                               watch_extra_clear)]
# watch_extra_6 = [x[0] + ' ' + x[1] for x in itertools.product(watch_series_clear,
#                                                               watch_extra_clear)]

# size_watch = '|'.join(watch_size_clear)
# check_names_watch = watch_extra_1 + watch_extra_2 + \
#                     watch_extra_3 + watch_extra_4 + \
#                     watch_extra_5 + watch_extra_6

# list_error_products = []
# color_tmp = None
# memory_tmp = None
# series_tmp = None
# cost_tmp = None
# ram_tmp = None
# model_tmp = None
# region_tmp = None

# class GetModelInfo:
#     def __init__(self, line):
#         self.line = line.lower().replace(' ', '')
#         self.line_tmp = line
#         # TODO Сделать замену специфики в строке

#     def get_info(self):
#         # Проверка на iPhone
#         global color_tmp
#         global memory_tmp
#         global series_tmp
#         global cost_tmp
#         global ram_tmp
#         global model_tmp
#         global region_tmp
#         for models in check_names_iphone:
#             models = models.replace(' ', '')
#             for i in self.line:
#                 if re.findall(country, i.lower()):
#                     region_tmp = 'Америка'
#                 if re.findall('россия|ростест|рос|🇷🇺', i.lower()):
#                     region_tmp = 'Ростест'
#             if models in self.line:
#                 model_tmp = 'iphone'
#                 memory = '64|128|256|512|1tb|1тб'
#                 if re.findall('[0-9]+', self.line):
#                     if int(re.findall('[0-9]+', self.line)[-1]) > 3000:
#                         cost_tmp = re.findall('[0-9]+', self.line)[-1]
#                         self.line = self.line.replace(cost_tmp, '')
#                 if re.findall(memory, self.line):
#                     memory_tmp = re.findall(memory, self.line)[0]
#                     self.line = self.line.replace(memory_tmp, '')
#                 if re.findall(colors, self.line):
#                     color_tmp = re.findall(colors, self.line)[0]
#                     self.line = self.line.replace(color_tmp, '')
#                 if re.findall(re_iphone, self.line):
#                     series_tmp = re.findall(re_iphone, self.line)[0]
#                     self.line = self.line.replace(series_tmp, '')

#                 check = [color_tmp, memory_tmp, series_tmp, cost_tmp, ]
#                 if None in check:
#                     return False

#                 if 'iphone' in series_tmp:
#                     series_tmp = series_tmp.replace('iphone', '')
#                 info = {'device': 'iphone',
#                         'color': color_tmp,
#                         'memory': memory_tmp,
#                         'series': series_tmp,
#                         'cost': cost_tmp,
#                         'ram': None,
#                         'extra': self.line_tmp,
#                         }
#                 color_tmp = None

#                 return info

#         # MacBook
#         for models in check_names_macbook:
#             models = models.lower().replace(' ', '')
#             if models in self.line:
#                 if re.findall('[0-9]+', self.line):
#                     if int(re.findall('[0-9]+', self.line)[-1]) > 3000:
#                         cost_tmp = re.findall('[0-9]+', self.line)[-1]
#                         self.line = self.line.replace(cost_tmp, '')

#                 if re.findall(re_macbook_memory, self.line):
#                     memory_tmp = re.findall(re_macbook_memory, self.line)[0]
#                     self.line = self.line.replace(memory_tmp, '')

#                 if re.findall(colors, self.line):
#                     color_tmp = re.findall(colors, self.line)[0]
#                     self.line = self.line.replace(color_tmp, '')

#                 if re.findall(re_macbook, self.line):

#                     series_tmp = re.findall(re_macbook, self.line)[0]
#                     self.line = self.line.replace(series_tmp, '')

#                 ram = '4|8|12|16|32'
#                 if re.findall(ram, self.line):
#                     ram_tmp = re.findall(ram, self.line)[-1]
#                     self.line = self.line.replace(ram_tmp, '')

#                 check = [color_tmp, memory_tmp, series_tmp, cost_tmp, ]
#                 if None in check:
#                     return False

#                 if 'macbook' in series_tmp:
#                     series_tmp = series_tmp.replace('macbook', '')

#                 info = {'device': 'macbook',
#                         'color': color_tmp,
#                         'memory': memory_tmp,
#                         'series': series_tmp,
#                         'cost': cost_tmp,
#                         'ram': ram_tmp,
#                         'extra': self.line_tmp,
#                         }
#                 color_tmp = None
#                 model_tmp = 'macbook'
#                 return info
#         if model_tmp:
#             if re.findall('[0-9]+', self.line):
#                 if int(re.findall('[0-9]+', self.line)[-1]) > 3000:
#                     cost_tmp = re.findall('[0-9]+', self.line)[-1]
#                     self.line = self.line.replace(cost_tmp, '')
#             if re.findall(colors, self.line):
#                 color_tmp = re.findall(colors, self.line)[0]
#                 self.line = self.line.replace(color_tmp, '')
#             check = [color_tmp, memory_tmp, series_tmp, cost_tmp, ]
#             if None in check:
#                 return False
#             info = {'device': model_tmp,
#                     'color': color_tmp,
#                     'memory': memory_tmp,
#                     'series': series_tmp,
#                     'cost': cost_tmp,
#                     'ram': ram_tmp,
#                     'extra': self.line_tmp,
#                     }
#             return info


# def generator(new_price):
#     global region_tmp
#     current_line = new_price.split('\n')
#     for i in current_line:
#         if re.findall(country, i.lower()):
#             region_tmp = 'Америка'
#         else:
#             region_tmp = 'Ростест'
#         line = re.sub('^\s+|\n|\r|\s+$', '', i)
#         line = re.sub(r'[^\w\s]', '', line)

#         yield line



# def clear_memory(memory):
#     word = 'tb|тб|гб|gb'
#     memory = re.sub(word, '', memory)
#     return memory


# def get_product_list(price):
#     exit_product = []
#     for line in generator(price):
#         if line != '':
#             models = GetModelInfo(line).get_info()
#             if models:
#                 models['memory'] = clear_memory(models['memory'])
#                 models['region'] = region_tmp
#                 print(models)
#                 exit_product.append(models)

#     return exit_product
