def is_overlap(rec_a_coord, rec_b_coord):
    xleft_bottom_a, yleft_bottom_a, xright_top_a, yright_top_a = rec_a_coord
    xleft_bottom_b, yleft_bottom_b, xright_top_b, yright_top_b = rec_b_coord
    print(xleft_bottom_a, yleft_bottom_a, xright_top_a, yright_top_a, xleft_bottom_b, yleft_bottom_b, xright_top_b, yright_top_b)

    '''l_bottom_a = xleft_bottom_a, yleft_bottom_a
    r_bottom_a = xright_top_a, yleft_bottom_a
    l_top_a = xleft_bottom_a, yright_top_a
    r_top_a = xright_top_a, yright_top_a'''

    top_a = yright_top_a
    bot_a = yleft_bottom_a
    lef_a = xleft_bottom_a
    rig_a = xright_top_a

    top_b = yright_top_b
    bot_b = yleft_bottom_b
    lef_b = xleft_bottom_b
    rig_b = xright_top_b

    t_y = 0
    b_y = 0
    l_x = 0
    r_x = 0

    #a ends beyond b on both sides
    if (top_a>=top_b and bot_a<bot_b):
        print('1')
        b_overlapped = 1.0
        a_overlapped = (top_b-bot_b)/(top_a-bot_a)
        t_y = top_b
        b_y = bot_b
    #a top beyond b but ends before bot b
    elif (top_a>=top_b and bot_a>=bot_b):
        print('2')
        b_overlapped = (top_b-bot_a)/(top_b-bot_b)
        a_overlapped = (top_b-bot_a)/(top_a-bot_a)
        t_y, b_y = top_b, bot_a
    #a ends within b
    elif (top_b>=top_a and bot_b<bot_a):
        print('3')
        b_overlapped = (top_a-bot_a)/(top_b-bot_b)
        a_overlapped = 1.0
        t_y, b_y = top_a, bot_a
    #a bots beyond b but tops within b
    elif (top_b>=top_a and bot_a<bot_b):
        print('4')
        b_overlapped = (top_b-bot_a)/(top_b-bot_b)
        a_overlapped = (top_b-bot_a)/(top_a-bot_a)
        t_y, b_y = top_a, bot_b

    print(b_overlapped, a_overlapped)

    #a ends beyond b on lefth sides
    if (rig_a>=rig_b and lef_a<lef_b):
        print('5')
        q_overlapped = 1.0
        p_overlapped = (rig_b-lef_b)/(rig_a-lef_a)
        l_x, r_x = lef_b, rig_b
    #a right beyond b but ends before left b
    elif (rig_a>=rig_b and lef_a>=lef_b):
        print('6')
        q_overlapped = (rig_b-lef_a)/(rig_b-lef_b)
        p_overlapped = (rig_b-lef_a)/(rig_a-lef_a)
        l_x, r_x = lef_a, rig_b
    #a ends within b
    elif (rig_b>=rig_a and lef_b<lef_a):
        print('7')
        q_overlapped = (rig_a-lef_a)/(rig_b-lef_b)
        p_overlapped = 1.0
        l_x, r_x = lef_a, rig_a
    #a lefts beyond b but rights within b
    elif (rig_b>=rig_a and lef_a<lef_b):
        print('8')
        q_overlapped = (rig_b-lef_a)/(rig_b-lef_b)
        p_overlapped = (rig_b-lef_a)/(rig_a-lef_a)
        l_x, r_x = lef_b, rig_a

    print(q_overlapped, p_overlapped)
    print((r_x, b_y), (l_x, t_y))
    return (r_x, b_y), (l_x, t_y)
