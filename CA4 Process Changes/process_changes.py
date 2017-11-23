def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data


def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ') [0],
                'time': details[2].strip().split(' ')[1],
                'number_of_lines': int(details[3].strip().split(' ')[0])
            }
            changed_file_end_index = data.index('', index + 1)
            commit ['changed_path'] = data[index + 3 : changed_file_end_index]
            commit ['comment'] = data[changed_file_end_index + 1 :
                        changed_file_end_index + 1 + commit ['number_of_lines']]
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            index = len(data)
    return commits

def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("revision, author, date, time, number_of_lines\n")
    for commit in commits:
        my_file.write(commit['revision'] + ',' + commit['author'] +
                ',' + commit['date'] + ',' + commit['time'] + ','  + 
                str(commit['number_of_lines']) + ',' + ' '.join(commit['comment']) + '\n')
    my_file.close()
            
    
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
    save_commits(commits, 'changes.csv')
    

        
        