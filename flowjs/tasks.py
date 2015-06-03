from __future__ import absolute_import


def join_chunks_task(flow_file):
    print 'starting join task',
    return flow_file._join_chunks()

def delete_chunks_task(flow_file):
    print 'starting delete task',
    return flow_file._delete_chunks()
