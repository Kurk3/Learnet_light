from flask import Blueprint, render_template

lectures = Blueprint('lectures', __name__)

@lectures.route('/lectures')
def main_lectures():
    return render_template('lectures/lectures_main.html')


@lectures.route('/historia_sieti')
def lecture_num1():
    return render_template('lectures/lecture_02.html')


@lectures.route('/pocitacove_siete')
def lecture_num2():
    return render_template('lectures/lecture_03.html')


@lectures.route('/referencny_model')
def lecture_num3():
    return render_template('lectures/lecture_04.html')


@lectures.route('/iso_osi_model')
def lecture_num4():
    return render_template('lectures/lecture_05.html')


@lectures.route('/tcp_ip_model')
def lecture_num5():
    return render_template('lectures/lecture_06.html')


@lectures.route('/osi_vs_tcp_ip_packet_transfer')
def lecture_num6():
    return render_template('lectures/lecture_07.html')


@lectures.route('/sietova_vrstva')
def lecture_num7():
    return render_template('lectures/lecture_08.html')


@lectures.route('/ip_adresy')
def lecture_num8():
    return render_template('lectures/lecture_09.html')


@lectures.route('/podsiete')
def lecture_num9():
    return render_template('lectures/lecture_10.html')


@lectures.route('/mac_adresy')
def lecture_num10():
    return render_template('lectures/lecture_11.html', )


@lectures.route('/ipv6_adresy')
def lecture_num11():
    return render_template('lectures/lecture_12.html')


@lectures.route('/sietove_topologie')
def lecture_num12():
    return render_template('lectures/lecture_13.html')

@lectures.route('/sietove_komponenty')
def lecture_num13():
    return render_template('lectures/lecture_14.html')


@lectures.route('/linkova_vrstva')
def lecture_num14():
    return render_template('lectures/lecture_15.html')


@lectures.route('/fyzicka_vrstva')
def lecture_num15():
    return render_template('lectures/lecture_16.html')


@lectures.route('/protokoly')
def lecture_num16():
    return render_template('lectures/lecture_17.html')
