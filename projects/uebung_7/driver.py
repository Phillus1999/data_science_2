from matrix_mr import MatrixMR
import json

if __name__ == '__main__':
    # Create an instance of the MatrixMR job
    mr_job = MatrixMR(args=['arxiv-metadata-oai-snapshot.json'])
    with mr_job.make_runner() as runner:
        runner.run()